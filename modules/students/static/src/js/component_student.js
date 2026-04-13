import { Component, useState, onWillStart, onWillRender, onMounted, useRef } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class StudentsComponent extends Component {
    // Le decimos a Odoo la vista/contenido que queremos pintar/renderizar
    static template = "students.view_calification_student";
    static props = {
        user_name: { type: String, optional: false },
        estudiante_Id: { type: Number, optional: true }
    }

    // Inicializa constructor del componente, uso de hooks
    setup() {
        this.ui = useService("ui") // Para pantallas de carga
        this.notification = useService("notification") // Para notificaciones
        this.state = useState({ number: 0, student: null, edad: 0, calificaciones: [] }) // Para cambios de estado
        this.orm = useService("orm") // Para acceder al ORM (search, read, browse, searchRead...)
        this.inputEdad = useRef("inputEdad")

        // El primero en ejecutarse en el renderizado. Permite 'async' y sirve para 
        // traernos información de la BD antes de pintar el xml
        onWillStart(async () => {
            if (!this.props.estudiante_id) {
                this.notification.add("No se recibió el estudiante_id", { type: "danger" })
                return
            }

            const student = await this.orm.searchRead("students.info", [["id", "=", this.props.estudiante_id]], ["edad"])

            if (!student || student.length === 0) {
                this.notification.add("No se encontro al estudiante", { type: "danger" })
                return
            }

            console.log(`Datos recibidos: ${student}`)
            this.state.student = student[0]
            this.state.edad = student[0].edad

            const califications = await this.orm.searchRead("students.calificaciones", [["estudiante_id", "=", this.props.estudiante_id]], ["asignatura_id", "profesor_id", "estado", "calificacion"])
            this.state.calificaciones = califications
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

    validarEdad() {
        // El -> Elemento del DOM y value, su valor
        const valueAge = parseInt(this.inputEdad.el.value)

        if (valueAge > 18) {
            this.notification.add('Edad no cumple los requisitos', { type: 'danger' })
            return
        }

        this.notification.add('Edad validada correctamente!')
    }
}

// Le pasamos el componente, siempre misma estructura
registry.category("public_components").add("students.student_component", StudentsComponent)