import { Component } from "@odoo/owl"
import { registry } from "@web/core/registry"

export class StudentsComponent extends Component {
    // Le decimos a Odoo la vista/contenido que queremos pintar/renderizar
    static template = "students.view_calification_student";

    // Inicializa constructor del componente
    setup() {
        console.log("Se ha cargado el componente")
    }
}

// Le pasamos el componente, siempre misma estructura
registry.category("public_components").add("students.student_component", StudentsComponent)