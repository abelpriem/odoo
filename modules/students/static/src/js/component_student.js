import { Component } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class StudentsComponent extends Component {
    // Le decimos a Odoo la vista/contenido que queremos pintar/renderizar
    static template = "students.view_calification_student";
    static props = {
        userName: { type: String, optional: false }
    }

    // Inicializa constructor del componente
    setup() {
        console.log("Se ha cargado el componente")
    }

    // Funciones
    openAlert() {
        alert("Prueba de alerta")
    }

    viewInput(event) {
        console.log(event.target.value)
    }
}

// Le pasamos el componente, siempre misma estructura
registry.category("public_components").add("students.student_component", StudentsComponent)