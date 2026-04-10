import { Component, useState, onWillStart, onWillRender, onMounted } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class StudentsComponent extends Component {
    // Le decimos a Odoo la vista/contenido que queremos pintar/renderizar
    static template = "students.view_calification_student";
    static props = {
        userName: { type: String, optional: false },
        estudiante_id: { type: Number, optional: false }
    }

    // Inicializa constructor del componente, uso de hooks
    setup() {
        this.ui = useService("ui") // Para pantallas de carga
        this.notification = useService("notification") // Para notificaciones
        this.state = useState({ number: 0, edad: 0 }) // Para cambios de estado
        this.orm = useService("orm") // Para acceder al ORM (search, read, browse, searchRead...)

        // El primero en ejecutarse en el renderizado. Permite 'async' y sirve para 
        // traernos información de la BD antes de pintar el xml
        onWillStart(() => {
            // console.log("Ejecutando...")
            // this.state.number += 10

            const student = this.orm.seachReadh("students.info", [["id", "=", this.props.estudiante_id]])

            if (!student) {
                this.notification.add("No se encontro al estudiante", { type: "danget" })
                return
            }

            console.log(student)
            this.state.edad = student[0].edad
        })

        // Se ejecuta ANTES del renderizado. Se dispara siempre
        onWillRender(() => {
            this.notification.add("cambio", { type: "success" })
            // console.log("Renderizando...")
        })

        // El último en ejecutarse del renderizado
        onMounted(() => {
            // console.log("On Mounted")
        })
    }

    // Funciones
    openAlert() {
        // alert("Prueba de alerta")
        this.ui.block()
        setTimeout(() => {
            this.ui.unblock()
        }, 5000)
    }

    viewInput(event) {
        console.log(event.target.value)
    }

    viewNotification() {
        // Tipos: 'success' y 'danger'
        this.notification.add('Mostrando notificacion', { type: "success" })
    }

    changeNumber() {
        this.state.number++
    }
}

// Le pasamos el componente, siempre misma estructura
registry.category("public_components").add("students.student_component", StudentsComponent)