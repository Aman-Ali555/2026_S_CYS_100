import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QLabel, QLineEdit, QSlider, QFrame,
                              QProgressBar, QScrollArea, QSizePolicy)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

# ─── Data Store ───────────────────────────────────────────────────
p_store = []
probable = []
name = ""
crnt = ""
pasat = ""

# ─── File Save ────────────────────────────────────────────────────
def save_to_file():
    filename = f"SPA_{name}.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Name: {name}\n")
        f.write(f"Current Situation: {crnt}\n")
        f.write(f"Past Situation: {pasat}\n")
        f.write("\nPossibilities & Probabilities:\n")
        for i in range(len(p_store)):
            f.write(f"  {i+1}. {p_store[i]} — {probable[i]:.2f}%\n")
        max_prob = max(probable)
        max_index = probable.index(max_prob)
        f.write(f"\nMost Probable: {p_store[max_index]} ({max_prob:.2f}%)\n")
        f.write("=" * 50 + "\n\n")

# ─── Probability Calculation ──────────────────────────────────────
def calculate_probability(ratings):
    total = sum(ratings)
    return [(r / total) * 100 for r in ratings]

# ══════════════════════════════════════════════════════════════════
# SCREEN CLASSES
# ══════════════════════════════════════════════════════════════════

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Welcome.ui", self)
        self.beginbtn.clicked.connect(self.go_next)

    def go_next(self):
        global name
        name = self.nameInput.text().strip()
        if not name:
            return
        self.hide()
        self.next = InstructionsScreen()
        self.next.show()


class InstructionsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("f_page.ui", self)
        self.welcomeLabel.setText(f"Welcome, {name}.")
        self.understandBtn.clicked.connect(self.go_next)

    def go_next(self):
        self.hide()
        self.next = CurrentSituationScreen()
        self.next.show()


class CurrentSituationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("S_page.ui", self)
        self.continueBtn.clicked.connect(self.go_next)
        self.currentText.textChanged.connect(self.update_count)

    def update_count(self):
        words = len(self.currentText.toPlainText().split())
        self.wordCount.setText(f"{words} / 200")
        self.currentProgressBar.setValue(min(words, 200))

    def go_next(self):
        global crnt
        text = self.currentText.toPlainText().strip()
        if not text or len(text.split()) > 200:
            return
        crnt = text
        self.hide()
        self.next = PastSituationScreen()
        self.next.show()


class PastSituationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("T_page.ui", self)
        self.continueBtn.clicked.connect(self.go_next)
        self.pastText.textChanged.connect(self.update_count)

    def update_count(self):
        words = len(self.pastText.toPlainText().split())
        self.wordCount.setText(f"{words} / 200")
        self.pastProgressBar.setValue(min(words, 200))

    def go_next(self):
        global pasat
        text = self.pastText.toPlainText().strip()
        if not text or len(text.split()) > 200:
            return
        pasat = text
        self.hide()
        self.next = LoadingScreen1()
        self.next.show()


class LoadingScreen1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("4_page.ui", self)
        self.progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(40)

    def tick(self):
        self.progress += 2
        if self.progress > 100:
            self.progress = 100
        self.loadingBar.setValue(self.progress)
        self.loadingPct.setText(f"{self.progress}%")
        if self.progress >= 100:
            self.timer.stop()
            QTimer.singleShot(400, self.go_next)

    def go_next(self):
        self.hide()
        self.next = SummaryScreen()
        self.next.show()


class SummaryScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("5_page.ui", self)
        self.currentText.setText(crnt)
        self.pastText.setText(pasat)
        self.proceedBtn.clicked.connect(self.go_next)

    def go_next(self):
        self.hide()
        self.next = PossibilitiesScreen()
        self.next.show()


class PossibilitiesScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("6_page.ui", self)
        self.count = 2
        self.input_fields = []
        self.countLabel.setText(str(self.count))

        # Setup scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scroll_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("border: none; background: transparent;")

        self.minusBtn.clicked.connect(self.dec)
        self.plusBtn.clicked.connect(self.inc)
        self.rateBtn.clicked.connect(self.go_next)

        self.rebuild()

    def rebuild(self):
        # Clear
        for i in reversed(range(self.scroll_layout.count())):
            w = self.scroll_layout.itemAt(i).widget()
            if w:
                w.deleteLater()
        self.input_fields = []
        self.countLabel.setText(str(self.count))

        for i in range(self.count):
            row = QHBoxLayout()
            num = QLabel(f"{i+1:02d}")
            num.setFixedWidth(30)
            num.setStyleSheet("color: #6b84a8; font-size: 10px; background: transparent;")
            le = QLineEdit()
            le.setPlaceholderText(f"Describe possibility {i+1}...")
            le.setStyleSheet("background-color: #081428; color: #dde4f0; border-radius: 10px; border: 1px solid rgba(20,184,166,0.12); padding: 10px; font-size: 11px;")
            le.setMinimumHeight(45)
            self.input_fields.append(le)
            row.addWidget(num)
            row.addWidget(le)
            wrapper = QWidget()
            wrapper.setStyleSheet("background: transparent;")
            wrapper.setLayout(row)
            self.scroll_layout.addWidget(wrapper)

        self.scroll_layout.addStretch()

    def dec(self):
        if self.count > 2:
            self.count -= 1
            self.rebuild()

    def inc(self):
        self.count += 1
        self.rebuild()

    def go_next(self):
        global p_store
        p_store.clear()
        for le in self.input_fields:
            text = le.text().strip()
            if not text:
                return
            p_store.append(text)
        self.hide()
        self.next = RatingsScreen()
        self.next.show()


class RatingsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("7_page.ui", self)
        self.sliders = []

        # Setup scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(12)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollLayout.setWidget(self.scroll_widget)
        self.scrollLayout.setWidgetResizable(True)
        self.scrollLayout.setStyleSheet("border: none; background: transparent;")

        for i, poss in enumerate(p_store):
            # Card
            card = QFrame()
            card.setStyleSheet("background-color: #081428; border-radius: 12px; border: 1px solid rgba(20,184,166,0.12);")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(20, 14, 20, 14)
            card_layout.setSpacing(8)

            # Top row
            top_row = QHBoxLayout()
            num_lbl = QLabel(f"{i+1:02d}")
            num_lbl.setStyleSheet("color: #6b84a8; font-size: 10px; background: transparent;")
            num_lbl.setFixedWidth(28)
            p_lbl = QLabel(poss)
            p_lbl.setStyleSheet("color: #dde4f0; font-size: 11px; font-weight: bold; background: transparent;")
            p_lbl.setWordWrap(True)
            val_lbl = QLabel("5")
            val_lbl.setStyleSheet("color: #facc15; font-size: 14px; font-weight: bold; background: transparent;")
            val_lbl.setFixedWidth(20)
            slash = QLabel("/10")
            slash.setStyleSheet("color: #6b84a8; font-size: 11px; background: transparent;")
            top_row.addWidget(num_lbl)
            top_row.addWidget(p_lbl)
            top_row.addStretch()
            top_row.addWidget(val_lbl)
            top_row.addWidget(slash)
            card_layout.addLayout(top_row)

            # Slider
            slider = QSlider(Qt.Horizontal)
            slider.setRange(1, 10)
            slider.setValue(5)
            slider.setStyleSheet("""
                QSlider::groove:horizontal { background: #2a3347; height: 6px; border-radius: 3px; }
                QSlider::handle:horizontal { background: white; width: 18px; height: 18px; margin: -6px 0; border-radius: 9px; }
                QSlider::sub-page:horizontal { background: #14b8a6; border-radius: 3px; }
            """)
            slider.valueChanged.connect(lambda v, lbl=val_lbl: lbl.setText(str(v)))
            card_layout.addWidget(slider)

            # Tick labels
            tick_row = QHBoxLayout()
            for t in range(1, 11):
                tl = QLabel(str(t))
                tl.setAlignment(Qt.AlignCenter)
                tl.setStyleSheet("color: #6b84a8; font-size: 8px; background: transparent;")
                tick_row.addWidget(tl)
            card_layout.addLayout(tick_row)

            self.sliders.append(slider)
            self.scroll_layout.addWidget(card)

        self.scroll_layout.addStretch()
        self.seeResultsBtn.clicked.connect(self.go_next)

    def go_next(self):
        global probable
        ratings = [s.value() for s in self.sliders]
        probable = calculate_probability(ratings)
        self.hide()
        self.next = LoadingScreen2()
        self.next.show()


class LoadingScreen2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("8_page.ui", self)
        self.progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(40)

    def tick(self):
        self.progress += 2
        if self.progress > 100:
            self.progress = 100
        self.loadingBar.setValue(self.progress)
        self.loadingPct.setText(f"{self.progress}%")
        if self.progress >= 100:
            self.timer.stop()
            QTimer.singleShot(400, self.go_next)

    def go_next(self):
        self.hide()
        self.next = ResultsScreen()
        self.next.show()


class ResultsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("9_page.ui", self)

        self.resultSubtitle.setText(f"Here are the probability outcomes for your situation, {name}.")

        paired = sorted(zip(probable, p_store), reverse=True)

        # Most probable
        self.mostProbableText.setText(paired[0][1])
        self.mostProbablePct.setText(f"{paired[0][0]:.1f}% probability based on your ratings")

        # Setup scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(12)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollLayout1.setWidget(self.scroll_widget)
        self.scrollLayout1.setWidgetResizable(True)
        self.scrollLayout1.setStyleSheet("border: none; background: transparent;")

        for i, (prob, poss) in enumerate(paired):
            is_top = (i == 0)
            card = QFrame()
            border_color = "#14b8a6" if is_top else "rgba(20,184,166,0.12)"
            card.setStyleSheet(f"background-color: #081428; border-radius: 12px; border: 1px solid {border_color};")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(20, 14, 20, 14)
            cl.setSpacing(8)

            row = QHBoxLayout()
            if is_top:
                tag = QLabel("TOP")
                tag.setStyleSheet("background-color: #14b8a6; color: #030f0e; border-radius: 4px; font-size: 8px; font-weight: bold; padding: 2px 6px;")
                tag.setFixedWidth(38)
                row.addWidget(tag)

            num = QLabel(f"{i+1:02d}")
            num.setStyleSheet("color: #6b84a8; font-size: 10px; background: transparent;")
            num.setFixedWidth(28)
            p_lbl = QLabel(poss)
            p_lbl.setStyleSheet("color: #dde4f0; font-size: 11px; background: transparent;")
            p_lbl.setWordWrap(True)
            pct_lbl = QLabel(f"{prob:.1f}%")
            pct_color = "#14b8a6" if is_top else "#dde4f0"
            pct_lbl.setStyleSheet(f"color: {pct_color}; font-size: 13px; font-weight: bold; background: transparent;")
            pct_lbl.setMinimumWidth(70)
            pct_lbl.setAlignment(Qt.AlignRight)
            row.addWidget(num)
            row.addWidget(p_lbl)
            row.addStretch()
            row.addWidget(pct_lbl)
            cl.addLayout(row)

            bar = QProgressBar()
            bar.setRange(0, 100)
            bar.setValue(int(prob))
            bar.setTextVisible(False)
            bar.setFixedHeight(6)
            bar_color = "#14b8a6" if is_top else "#2a3347"
            bar.setStyleSheet(f"QProgressBar {{ background-color: #2a3347; border-radius: 3px; }} QProgressBar::chunk {{ background-color: {bar_color}; border-radius: 3px; }}")
            cl.addWidget(bar)
            self.scroll_layout.addWidget(card)

        self.scroll_layout.addStretch()
        self.saveBtn.clicked.connect(self.save)
        self.newAnalysisBtn.clicked.connect(self.new_analysis)

    def save(self):
        save_to_file()
        QtWidgets.QMessageBox.information(self, "Saved!", f"Results saved to SPA_{name}.txt")

    def new_analysis(self):
        global p_store, probable, crnt, pasat
        p_store.clear()
        probable.clear()
        crnt = ""
        pasat = ""
        self.hide()
        self.next = WelcomeScreen()
        self.next.show()


# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())
