<!--
  Componente reutilizável de formulário de filtro
  
  Como usar:
  
  <FilterForm @submit="handleFilter">
    <template #filters>
      <div class="col-12 col-md-3">
        <label class="form-label">Nome</label>
        <input type="text" class="form-control" v-model="filtros.nome" />
      </div>
      <div class="col-12 col-md-3">
        <label class="form-label">Email</label>
        <input type="text" class="form-control" v-model="filtros.email" />
      </div>
    </template>
  </FilterForm>
  
  Você pode adicionar quantos filtros quiser dentro do slot #filters
  O botão de pesquisar sempre ficará no final, alinhado com os inputs
-->

<script setup>
import { BRow, BButton } from "bootstrap-vue-next";
import { onMounted, onUnmounted } from "vue";

// Define os emits para o componente pai
const emit = defineEmits(['submit']);

// Função que será chamada quando o botão for clicado
function handleSubmit() {
  emit('submit');
}

// Adiciona listener para Enter nos inputs
function handleKeyDown(event) {
  // Se pressionar Enter dentro de um input do filtro
  if (event.key === 'Enter' && event.target.tagName === 'INPUT') {
    event.preventDefault();
    handleSubmit();
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeyDown);
});

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeyDown);
});
</script>

<template>
  <BRow class="mb-3 align-items-end">
    <!-- Slot para os campos de filtro -->
    <slot name="filters"></slot>
    
    <!-- Botão de pesquisar sempre no final -->
    <div class="col-12 col-md-auto mt-2 mt-md-0">
      <BButton @click="handleSubmit" variant="dark">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
        </svg>
        Pesquisar
      </BButton>
    </div>
  </BRow>
</template>

<style scoped>
/* Estilos opcionais podem ser adicionados aqui */
</style>
