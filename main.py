from PySide6.QtWidgets import( 
    QApplication,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget
)                                                
                                                  
                                                  
                                                  
                                                  
app = QApplication([])


window = QWidget()
window.setWindowTitle("Adaptive Gym Planner")
window.resize(800, 600)


layout = QVBoxLayout()

title = QLabel("Adaptive Gym Planner")

exercise_input = QLineEdit()
exercise_input.setPlaceholderText("Enter exercise name...")

weight_input = QLineEdit()
weight_input.setPlaceholderText("Weight (kg)...")

reps_input = QLineEdit()
reps_input.setPlaceholderText("Reps...")

add_set_button = QPushButton("Add Set")

sets_list = QListWidget()

def add_set():
    exercise = exercise_input.text()
    weight = weight_input.text()
    reps = reps_input.text()

    if exercise and weight and reps:
        set_info = f"{exercise}: {weight} kg x {reps} reps"
        sets_list.addItem(set_info)

        # Clear inputs after adding
        exercise_input.clear()
        weight_input.clear()
        reps_input.clear()

add_set_button.clicked.connect(add_set)

layout.addWidget(title)
layout.addWidget(exercise_input)
layout.addWidget(weight_input)
layout.addWidget(reps_input)
layout.addWidget(sets_list)
layout.addWidget(add_set_button)

window.setLayout(layout)

window.show()

app.exec()
