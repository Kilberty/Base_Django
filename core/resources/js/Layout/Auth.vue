<template>
  <div class="min-vh-100" style="background-color: #f4f4f9">
    <BNavbar type="light" variant="white" class="border-bottom">
      <BContainer class="d-flex justify-content-between align-items-center">
        <div class="d-flex align-items-center gap-3">
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
          <!-- Link Cadastros visível em sm+ -->
          <BButton
            class="d-none d-sm-block text-dark  text-decoration-none"
            variant="link"
            @click="toggleCadastros"
            :class="{ 'fw-bold text-primary': openCadastros }"
          >
            Cadastros
          </BButton>
        </div>

        <BDropdown variant="link" toggle-class="text-dark" :text="nome" right>
          <BDropdownItem href="/usuarios/logout">Log Out</BDropdownItem>
        </BDropdown>
      </BContainer>
    </BNavbar>

    <!-- Submenu Desktop Cadastros -->
    <div v-if="openCadastros" class="d-none d-sm-block border-bottom bg-white shadow-sm">
      <BContainer class="d-flex gap-3 py-2">
        <BLink href="/usuarios/" class="text-decoration-none text-dark submenu-link">Usuários</BLink>
    
      </BContainer>
    </div>

    <!-- Sidebar Offcanvas para xs -->
    <BOffcanvas
      v-model="showOffcanvas"
      title="Menu"
      placement="start"
    >
      <BNavbarNav class="flex-column">
        <div>
          <BButton
            variant="link"
            class="text-start text-dark text-decoration-none w-100"
            @click="toggleCadastrosMobile"
          >
            Cadastros
          </BButton>
          <div v-if="openCadastrosMobile" class="ps-4 py-2 d-flex flex-column gap-2 submenu-mobile">
            <BLink href="/usuarios/" class="text-decoration-none text-dark submenu-link">
              <span class="me-2">└</span>Usuários
            </BLink>
            
          </div>
        </div>
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
  BNavItem,
  BLink
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

// Estado para controlar o submenu de cadastros (desktop)
const openCadastros = ref(false);

// Estado para controlar o submenu de cadastros (mobile)
const openCadastrosMobile = ref(false);

// Função para toggle do submenu desktop
const toggleCadastros = () => {
  openCadastros.value = !openCadastros.value;
};

// Função para toggle do submenu mobile
const toggleCadastrosMobile = () => {
  openCadastrosMobile.value = !openCadastrosMobile.value;
};
</script>

<style scoped>
/* Estilo para hover nos links do submenu */
.submenu-link {
  transition: color 0.2s ease;
}

.submenu-link:hover {
  color: #0d6efd !important;
}

/* Estilo para o submenu mobile com borda à esquerda */
.submenu-mobile {
  border-left: 2px solid #0d6efd;
  margin-left: 1rem;
  background-color: #f8f9fa;
}
</style>
