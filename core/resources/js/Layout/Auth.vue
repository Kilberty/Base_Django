<template>
  <div class="min-vh-100" style="background-color: #f4f4f9">
    <BNavbar type="light" variant="white" class="border-bottom">
      <BContainer class="d-flex justify-content-between align-items-center">
        <div class="d-flex align-items-center gap-2">
          <BNavbarBrand class="d-none d-sm-block" href="/home">
            <img src="" height="20" alt="Logo" />
          </BNavbarBrand>
          <!-- Botão hamburguer para xs -->
          <BButton 
            class="d-block d-sm-none navbar-toggler" 
            @click="showOffcanvas = true"
            variant="outline-secondary"
          >
            <span class="navbar-toggler-icon"></span>
          </BButton>
          <!-- Dropdown Cadastros visível em sm+ -->
          <BDropdown
            class="d-none d-sm-block"
            variant="link"
            text="Cadastros"
            toggle-class="text-dark"
          >
            <BDropdownItem href="/usuarios/">Usuários</BDropdownItem>
          </BDropdown>
        </div>

        <BDropdown variant="link" toggle-class="text-dark" :text="nome" right>
          <BDropdownItem href="/usuarios/logout">Log Out</BDropdownItem>
        </BDropdown>
      </BContainer>
    </BNavbar>

    <!-- Sidebar Offcanvas para xs -->
    <BOffcanvas
      v-model="showOffcanvas"
      title="Menu"
      placement="start"
    >
      <BNavbarNav>
        <BNavItem href="/usuarios/">Usuários</BNavItem>
        <!-- Adicione outros itens do menu aqui -->
      </BNavbarNav>
    </BOffcanvas>

    <div class="bg-white shadow-sm py-3 border-bottom">
      <BContainer class="d-flex justify-content-between align-items-center">
        <h4 class="mb-0">{{ titulo }}</h4>
        <div class="d-flex gap-2">
          <Modal
            v-if="cadastro"
            :model-value="estado"
            @update:modelValue="$emit('update:estado', $event)"
            :title="titulo_modal"
            :onSave="modalOnSave"
          >
            <slot name="modal-body" />
          </Modal>

          <BButton v-if="cadastro" variant="danger">Excluir</BButton>
          <BButton v-if="info" variant="dark">Salvar</BButton>
          <BButton v-if="info" variant="danger">Excluir</BButton>
        </div>
      </BContainer>
    </div>

    <main class="py-4" style="min-height: calc(100vh - 180px);">
      <BContainer fluid="sm" class="bg-white border rounded p-3 p-md-4 d-flex flex-column" style="min-height: 700px;">
        <slot />
      </BContainer>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  BNavbar,
  BContainer,
  BNavbarBrand,
  BDropdown,
  BDropdownItem,
  BButton,
  BOffcanvas,
  BNavbarNav,
  BNavItem
} from "bootstrap-vue-next";
import Modal from "../Partials/Modal.vue";

const props = defineProps({
  titulo: String,
  nome: String,
  cadastro: Boolean,
  info: Boolean,
  titulo_modal: String,
  estado: Boolean,
  modalOnSave: { type: Function, default: null },
});

const emit = defineEmits(["update:estado"]);

// Estado para controlar o offcanvas
const showOffcanvas = ref(false);
</script>

<style>
/* estilos opcionais */
</style>
