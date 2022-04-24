<template>
  <div
    class="shadow-xl w-10/12 mt-5 flex flex-col justify-center gap-4 items-center w-full rounded-xl pb-4"
  >
    <div class="w-full">
      <step-progress
        :steps="steps"
        :current-step="currentStep"
        icon-class="fa fa-check"
        active-color="blue"
      ></step-progress>
    </div>
    <h1 v-if="currentStep === 0" class="text-4xl mb-4">
      Registrar nueva historia clinica
    </h1>
    <FormUserInfo v-if="currentStep === 1" />
    <ConsultReason v-if="currentStep === 2" />
    <UserAnnexes v-if="currentStep === 3" />

    <div class="flex gap-5">
      <vs-button type="filled" @click="back" v-if="currentStep > 0">
        <box-icon name="left-arrow" type="solid" color="#fff"></box-icon
        >Anterior</vs-button
      >
      <div v-if="currentStep < 4">
        <vs-button type="filled" @click="next"
          >Siguiente
          <box-icon name="right-arrow" type="solid" color="#fff"></box-icon
        ></vs-button>
      </div>
      <div v-else>
        <vs-button size="xl" success type="filled" @click="register"
          >Registrar</vs-button
        >
      </div>
    </div>
  </div>
</template>
<script>
import StepProgress from "vue-step-progress";
import "vue-step-progress/dist/main.css";
import FormUserInfo from "./FormUserInfo.vue";
import ConsultReason from "./ConsultReason.vue";
import UserAnnexes from "./UserAnnexes.vue";
export default {
  components: {
    "step-progress": StepProgress,
    FormUserInfo,
    ConsultReason,
    UserAnnexes,
  },
  data() {
    return {
      steps: [
        "Inicio",
        "Datos del paciente",
        "Datos de la consulta",
        "Anexos",
        "Enviar",
      ],
      currentStep: 0,
      notification: null,
    };
  },
  methods: {
    next() {
      this.currentStep++;
    },
    back() {
      this.currentStep--;
    },
    register() {
      this.openNotification("success", "Exitoso");
    },
    openNotification(color, text) {
      this.notification = this.$vs.notification({
        color,
        flat: true,
        position: "top-right",
        title: "Registro de historia clinica",
        text,
      });
    },
  },
};
</script>
<style>
.step-progress__step-label {
  font-size: 10px;
}
.step-progress__step:after {
  width: 50px;
  height: 50px;
}
.step-progress__step span {
  font-size: 30px;
}
</style>
