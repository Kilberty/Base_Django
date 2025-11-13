<template>
  <BButton variant="dark" @click="estadoLocal = true">Adicionar</BButton>

  <BModal v-model="estadoLocal" size="lg" :title="title">
    <slot />
    <template #footer>
        <BButton variant="danger" @click="estadoLocal = false">Cancelar</BButton>
        <BButton variant="dark" @click="handleSaveAndClose">Salvar</BButton>
    </template>
  </BModal>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from "vue";
import { BButton, BModal } from "bootstrap-vue-next";
const props = defineProps({
  title: { type: String, default: "Modal" },
  onSave: { type: Function, default: null },
  modelValue: { type: Boolean, default: false },
});
const emit = defineEmits(["update:modelValue"]);

const estadoLocal = ref(props.modelValue);

watch(estadoLocal, (val) => emit("update:modelValue", val));
watch(() => props.modelValue, (val) => (estadoLocal.value = val));
function handleSaveAndClose() {
  if (props.onSave) props.onSave();
  // Não fecha o modal aqui - deixa o componente pai controlar o fechamento
}




</script>