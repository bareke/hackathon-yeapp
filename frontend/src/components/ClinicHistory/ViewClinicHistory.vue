<template>
  <div class="flex gap-6">
    <vs-button danger flat class="absolute right-4 my-4" @click="generateReport"
      >Generar reporte</vs-button
    >
    <div class="center">
      <vs-button
        success
        flat
        class="absolute right-40 my-4"
        @click="active = !active"
        >Analizar historia</vs-button
      >
      <vs-dialog scroll overflow-hidden not-close auto-width v-model="active">
        <template #header>
          <h3>
            <b
              >Recomendaciones teniendo en cuenta tu reciente historial
              clínico</b
            >
          </h3>
        </template>
        <div class="con-content">
          <h4>
            <b>{{ this.recommendations.title }}</b>
          </h4>
          <p>
            {{ this.recommendations.description }}
          </p>
          <br />
          <br />
          <h4>
            <b>{{ this.recommendations.limits.title }}</b>
          </h4>

          <br />

          <p>
            {{ this.recommendations.limits.recommendations[0].title }}
            <br />
            <br />
            {{ this.recommendations.limits.recommendations[0].description }}

            <br />
            <br />

            {{ this.recommendations.limits.recommendations[1].title }}
            <br />
            <br />
            {{ this.recommendations.limits.recommendations[1].description }}
          </p>

          <vs-button text-center success flat @click="scheduleAppointment"
            >Agendar cita</vs-button
          >
        </div>
      </vs-dialog>
    </div>
    <AccordeonComponent
      class="mt-16"
      ref="user"
      title="Información del paciente"
    >
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Nombres del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.name }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Apellidos del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.lastname }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Identificación del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.identificationNumber }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Dirección del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.address }}</span>
      </div>
    </AccordeonComponent>
    <AccordeonComponent
      class="mt-16"
      id="consult"
      title="Información de la consulta"
    >
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Descripción:</b></span>
        <span>{{ clinicHistory.node.data.consultData.description }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Enfermedades:</b></span>
        <span>{{ clinicHistory.node.data.consultData.actualSicks }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Antecedentes:</b></span>
        <span>{{ clinicHistory.node.data.consultData.past }}</span>
      </div>
    </AccordeonComponent>
    <AccordeonComponent class="mt-16" id="annexes" title="Anexos">
      <h1>No hay anexos</h1></AccordeonComponent
    >
  </div>
</template>

<script>
import AccordeonComponent from "@/components/AccordeonComponent.vue";

export default {
  components: { AccordeonComponent },
  props: ["clinicHistory"],
  data() {
    return {
      active: false,
      recommendations: "",
    };
  },
  created() {
    const option = "colesterol";
    const description = this.clinicHistory.node.data.consultData.description;
    if (description.includes(option)) {
      this.recommendations = {
        title: "¿Qué es el colesterol?",
        description:
          "Su cuerpo necesita algo de colesterol para funcionar bien. Pero si tiene demasiado colesterol en la sangre, se puede pegar en las paredes de sus arterias, estrechándolas o incluso bloqueándolas. Esto lo pone en riesgo de enfermedad de las arterias coronarias y otras enfermedades del corazón.",
        limits: {
          title: "¿Cómo puedo bajar el colesterol con la dieta?",
          recommendations: [
            {
              title: "Limite la sal.",
              description: `Debe intentar limitar la cantidad de sodio (sal) que consume a no más de 2,300 miligramos (aproximadamente una cucharadita de sal) por día. Eso incluye toda la sal que consume, ya sea que se haya agregado en la cocina o en la mesa, o que ya esté presente en los productos alimenticios. Limitar la sal no reducirá el colesterol, pero puede bajar el riesgo de enfermedades cardíacas al ayudar a reducir la presión arterial. Puede reducir la sal eligiendo alimentos con bajo contenido de sal y "sin sal agregada", además de preferir condimentos en la mesa o al cocinar en vez de sal.`,
            },
            {
              title: "Limite el alcohol.",
              description:
                "El alcohol añade calorías adicionales, las que pueden llevar al aumento de peso. Tener sobrepeso puede elevar su nivel de colesterol malo y disminuir su nivel de colesterol bueno. Demasiado alcohol también puede aumentar su riesgo de enfermedades del corazón, porque puede elevar su presión arterial y el nivel de triglicéridos.",
            },
          ],
        },
      };
    }
  },
  methods: {
    generateReport() {
      this.launchNotification(
        "success",
        "Generando reporte ...",
        "",
        '<box-icon color="rgb(20,255,20)" type="solid" name="newUser-check"></box-icon>'
      );
    },
    scheduleAppointment() {
      this.launchNotification(
        "success",
        "Programando cita preventiva ...",
        "",
        '<box-icon color="rgb(20,255,20)" type="solid" name="newUser-check"></box-icon>'
      );
    },
    launchNotification(color = "success", title = "", body = "", icon = "") {
      this.$vs.notification({
        position: "top-right",
        color,
        flat: true,
        icon,
        progress: "auto",
        title,
        text: body,
      });
    },
  },
};
</script>
