# FilterForm Component - Documentação

## Descrição
Componente reutilizável de formulário de filtro com botão de pesquisa automático.

## Localização
`/core/resources/js/Components/FilterForm.vue`

## Como usar

### Exemplo básico (1 filtro) - COM INERTIA
```vue
<script setup>
import FilterForm from "../Components/FilterForm.vue";
import { useForm } from "@inertiajs/vue3";

// Use useForm do Inertia para os filtros
const formFiltro = useForm({
  nome: ""
});

function handleFilter() {
  // Use .get() para fazer requisição GET com query params
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
</script>

<template>
  <FilterForm @submit="handleFilter">
    <template #filters>
      <div class="col-12 col-md-3">
        <label class="form-label">Nome</label>
        <input type="text" class="form-control" v-model="formFiltro.nome" />
      </div>
    </template>
  </FilterForm>
</template>
```

### Exemplo com múltiplos filtros - COM INERTIA
```vue
<script setup>
import FilterForm from "../Components/FilterForm.vue";
import { useForm } from "@inertiajs/vue3";

// Sempre use useForm do Inertia, NÃO use ref() para filtros
const formFiltro = useForm({
  nome: "",
  email: "",
  status: "",
  dataInicio: "",
  dataFim: ""
});

function handleFilter() {
  // O Inertia automaticamente remove campos vazios da URL
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
</script>

<template>
  <FilterForm @submit="handleFilter">
    <template #filters>
      <div class="col-12 col-md-3">
        <label class="form-label">Nome</label>
        <input 
          type="text" 
          class="form-control" 
          placeholder="Digite o nome"
          v-model="formFiltro.nome" 
        />
      </div>
      
      <div class="col-12 col-md-3">
        <label class="form-label">Email</label>
        <input 
          type="email" 
          class="form-control" 
          placeholder="Digite o email"
          v-model="formFiltro.email" 
        />
      </div>
      
      <div class="col-12 col-md-2">
        <label class="form-label">Status</label>
        <select class="form-control" v-model="formFiltro.status">
          <option value="">Todos</option>
          <option value="ativo">Ativo</option>
          <option value="inativo">Inativo</option>
        </select>
      </div>
      
      <div class="col-12 col-md-2">
        <label class="form-label">Data Início</label>
        <input 
          type="date" 
          class="form-control" 
          v-model="formFiltro.dataInicio" 
        />
      </div>
      
      <div class="col-12 col-md-2">
        <label class="form-label">Data Fim</label>
        <input 
          type="date" 
          class="form-control" 
          v-model="formFiltro.dataFim" 
        />
      </div>
    </template>
  </FilterForm>
</template>
```

### Exemplo com componente Input customizado - COM INERTIA
```vue
<script setup>
import FilterForm from "../Components/FilterForm.vue";
import Input from "../Components/Input.vue";
import { useForm } from "@inertiajs/vue3";

const formFiltro = useForm({
  nome: "",
  cpf: ""
});

function handleFilter() {
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
</script>

<template>
  <FilterForm @submit="handleFilter">
    <template #filters>
      <div class="col-12 col-md-4">
        <Input 
          label="Nome Completo" 
          type="text"
          v-model="formFiltro.nome"
          placeholder="Digite o nome"
        />
      </div>
      
      <div class="col-12 col-md-3">
        <Input 
          label="CPF" 
          type="text"
          v-model="formFiltro.cpf"
          placeholder="000.000.000-00"
        />
      </div>
    </template>
  </FilterForm>
</template>
```

### ⚠️ IMPORTANTE: Separar form de cadastro e form de filtro

```vue
<script setup>
import { useForm } from "@inertiajs/vue3";

// Form para CADASTRO (POST)
const form = useForm({
  nome: "",
  email: "",
  password: ""
});

// Form para FILTRO (GET) - SEMPRE SEPARADO!
const formFiltro = useForm({
  nome: "",
  email: ""
});

function handleSave() {
  form.post('/usuarios/cadastrar/', {
    onSuccess: () => form.reset()
  });
}

function handleFilter() {
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
</script>
```

## Props
Nenhuma prop necessária.

## Events
- `@submit`: Emitido quando o botão de pesquisa é clicado ou quando o form é submetido (Enter)

## Slots
- `#filters`: Slot onde você coloca todos os campos de filtro. Cada campo deve estar dentro de uma div com classes de coluna do Bootstrap (`col-12 col-md-X`)

## Características
✅ Botão de pesquisa automático com ícone de lupa
✅ Alinhamento automático dos campos
✅ Responsivo (mobile e desktop)
✅ Suporta Enter para submeter
✅ Totalmente customizável

## Notas importantes
1. **SEMPRE use `useForm` do Inertia para filtros, NUNCA use `ref()`**
2. **Separe o form de cadastro (`form`) do form de filtro (`formFiltro`)**
3. Use `formFiltro.get()` para filtros (GET) e `form.post()` para cadastros (POST)
4. Sempre use `col-12` para mobile e `col-md-X` para desktop
5. O botão sempre ficará no final, alinhado com a base dos inputs
6. Use `v-model` vinculando diretamente ao `formFiltro.campo`
7. `preserveState: true` mantém o estado da página durante o filtro
8. `preserveScroll: true` mantém a posição do scroll durante o filtro

## Vantagens de usar useForm do Inertia
✅ Gerenciamento automático de loading state
✅ Tratamento de erros integrado
✅ Remove automaticamente campos vazios da URL
✅ Sincronização automática com o backend
✅ Suporte nativo a `preserveState` e `preserveScroll`
