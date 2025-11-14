# Input Component - Documentação de Responsividade

## Localização
`/core/resources/js/Components/Input.vue`

## Props disponíveis

### Props básicas
- `id`: String - ID do input
- `name`: String - Nome do input
- `label`: String - Label que aparece acima do input
- `type`: String - Tipo do input (text, email, password, date, etc.)
- `modelValue`: String/Number - Valor do input (usado com v-model)
- `placeholder`: String - Placeholder do input

### Props de responsividade (Bootstrap Grid)
- `cols`: String/Number - Tamanho para **mobile (xs)** - **PADRÃO: "12"** (100% da largura)
- `sm`: String/Number - Tamanho para telas small (≥576px)
- `md`: String/Number - Tamanho para telas medium (≥768px)
- `lg`: String/Number - Tamanho para telas large (≥992px)
- `xl`: String/Number - Tamanho para telas extra large (≥1200px)

**IMPORTANTE:** 
- ❌ **NÃO existe `xs`** no Bootstrap 5! 
- ✅ Use `cols` para controlar o mobile (xs)
- ✅ Se você não passar `cols`, o padrão é `"12"` (100% da largura no mobile)

## Como usar

### Exemplo 1: Apenas mobile (100% da largura)
```vue
<Input 
  type="text" 
  name="nome"
  id="nome"
  label="Nome"
  v-model="form.nome"
/>
```
**Resultado:** Sempre ocupa 100% da largura em todas as telas (cols="12" é padrão)

---

### Exemplo 2: Responsivo (mobile 100%, desktop 50%)
```vue
<Input 
  type="text" 
  name="nome"
  id="nome"
  label="Nome"
  md="6"
  v-model="form.nome"
/>
```
**Resultado:**
- Mobile (xs): 100% da largura (cols="12" padrão)
- Desktop (md+): 50% da largura (6 colunas)

---

### Exemplo 3: Totalmente responsivo
```vue
<Input 
  type="text" 
  name="nome"
  id="nome"
  label="Nome Completo"
  placeholder="Digite seu nome"
  sm="6"
  md="4"
  lg="3"
  v-model="form.nome"
/>
```
**Resultado:**
- Mobile (xs): 100% da largura (cols="12" padrão)
- Small (sm): 50% da largura (6 colunas)
- Medium (md): 33% da largura (4 colunas)
- Large (lg+): 25% da largura (3 colunas)

---

### Exemplo 4: Controlando mobile explicitamente
```vue
<Input 
  type="text" 
  name="telefone"
  id="telefone"
  label="Telefone"
  placeholder="(00) 00000-0000"
  cols="6"
  md="3"
  v-model="form.telefone"
/>
```
**Resultado:**
- Mobile (xs): 50% da largura (6 colunas) - **2 campos por linha no mobile!**
- Desktop (md+): 25% da largura (3 colunas)

**Use caso:** Campos pequenos como CEP, DDD, etc. que podem ficar lado a lado no mobile

---

### Exemplo 5: Filtros responsivos (recomendado)
```vue
<FilterForm @submit="handleFilter">
  <template #filters>
    <Input 
      type="text" 
      name="filtroNome"
      id="filtroNome"
      label="Nome"
      placeholder="Digite o nome"
      md="3"
      v-model="formFiltro.nome"
    />
    
    <Input 
      type="email" 
      name="filtroEmail"
      id="filtroEmail"
      label="Email"
      placeholder="Digite o email"
      md="3"
      v-model="formFiltro.email"
    />
    
    <Input 
      type="date" 
      name="filtroData"
      id="filtroData"
      label="Data"
      md="2"
      v-model="formFiltro.data"
    />
  </template>
</FilterForm>
```
**Resultado:**
- Mobile: Cada campo ocupa 100% (empilhados verticalmente) - cols="12" padrão
- Desktop: Nome e Email ocupam 25% cada, Data ocupa 16.6%

---

## Exemplo completo em Usuarios.vue

```vue
<script setup>
import Input from "../Components/Input.vue";
import FilterForm from "../Components/FilterForm.vue";
import { useForm } from "@inertiajs/vue3";

const formFiltro = useForm({
  nome: "",
  email: "",
  status: ""
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
      <!-- Mobile: 100%, Desktop: 33% -->
      <Input 
        type="text" 
        name="filtroNome"
        id="filtroNome"
        label="Nome"
        placeholder="Digite o nome"
        cols="12"
        md="4"
        v-model="formFiltro.nome"
      />
      
      <!-- Mobile: 100%, Desktop: 33% -->
      <Input 
        type="email" 
        name="filtroEmail"
        id="filtroEmail"
        label="Email"
        placeholder="Digite o email"
        cols="12"
        md="4"
        v-model="formFiltro.email"
      />
      
      <!-- Mobile: 100%, Desktop: 33% -->
      <Input 
        type="text" 
        name="filtroStatus"
        id="filtroStatus"
        label="Status"
        cols="12"
        md="4"
        v-model="formFiltro.status"
      />
    </template>
  </FilterForm>
</template>
```

---

## Tabela de referência de colunas

| Colunas | Largura | Uso recomendado |
|---------|---------|------------------|
| 12 | 100% | Campo único, mobile |
| 6 | 50% | Dois campos por linha |
| 4 | 33.33% | Três campos por linha |
| 3 | 25% | Quatro campos por linha |
| 2 | 16.66% | Seis campos por linha |
| 1 | 8.33% | Doze campos por linha |

---

## Breakpoints do Bootstrap

| Breakpoint | Largura mínima | Dispositivo | Prop do Input |
|------------|----------------|-------------|---------------|
| xs | < 576px | Mobile portrait | `cols` |
| sm | ≥ 576px | Mobile landscape | `sm` |
| md | ≥ 768px | Tablet | `md` |
| lg | ≥ 992px | Desktop | `lg` |
| xl | ≥ 1200px | Desktop large | `xl` |

**IMPORTANTE:** Para controlar mobile (xs), use `cols` ao invés de `xs`!

---

## Controle de Mobile (xs)

### Padrão: 100% da largura (empilhado)
```vue
<!-- Não precisa passar nada, cols="12" é padrão -->
<Input label="Nome" v-model="form.nome" />
<Input label="Email" v-model="form.email" />
```
**Mobile:** Cada campo ocupa 100% (empilhados verticalmente)

### Dois campos por linha no mobile
```vue
<!-- Use cols="6" para 50% da largura -->
<Input cols="6" label="DDD" v-model="form.ddd" />
<Input cols="6" label="Telefone" v-model="form.telefone" />
```
**Mobile:** Dois campos lado a lado, cada um com 50%

### Três campos por linha no mobile
```vue
<!-- Use cols="4" para 33% da largura -->
<Input cols="4" label="Dia" v-model="form.dia" />
<Input cols="4" label="Mês" v-model="form.mes" />
<Input cols="4" label="Ano" v-model="form.ano" />
```
**Mobile:** Três campos lado a lado, cada um com 33%

### Exemplo completo com mobile customizado
```vue
<BRow>
  <!-- CEP: 40% no mobile, 25% no desktop -->
  <Input 
    cols="5" 
    md="3" 
    label="CEP" 
    v-model="form.cep" 
  />
  
  <!-- Estado: 30% no mobile, 16% no desktop -->
  <Input 
    cols="3" 
    md="2" 
    label="UF" 
    v-model="form.uf" 
  />
  
  <!-- Cidade: 100% no mobile, 58% no desktop -->
  <Input 
    cols="12" 
    md="7" 
    label="Cidade" 
    v-model="form.cidade" 
  />
</BRow>
```

---

## Dicas de uso

1. **NÃO precisa passar `cols="12"`** - já é o valor padrão!
2. **Use apenas `md`, `sm`, `lg`** para controlar responsividade
3. **Campos curtos (data, status)**: use `md="2"` ou `md="3"`
4. **Campos médios (nome, email)**: use `md="3"` ou `md="4"`
5. **Campos longos (descrição, observação)**: use `md="6"` ou não passe nada (fica 100%)
6. **Dentro de BRow**: O Input já cria um BCol, não precisa envolver em outra div

---

## Padrões recomendados

### Formulário de cadastro (modal)
```vue
<!-- Nome completo: 100% sempre -->
<Input label="Nome" v-model="form.nome" />

<!-- Email e Telefone: 50% cada em desktop -->
<Input md="6" label="Email" v-model="form.email" />
<Input md="6" label="Telefone" v-model="form.telefone" />

<!-- Senha e Confirmar: 50% cada -->
<Input md="6" type="password" label="Senha" v-model="form.password" />
<Input md="6" type="password" label="Confirmar" v-model="form.password2" />
```

### Formulário de filtro
```vue
<!-- 3 filtros: 33% cada em desktop -->
<Input md="4" label="Nome" v-model="formFiltro.nome" />
<Input md="4" label="Email" v-model="formFiltro.email" />
<Input md="4" label="Status" v-model="formFiltro.status" />
```

---

## 📱 Guia Rápido de Controle Mobile

| Objetivo | Props | Resultado |
|----------|-------|-----------|
| 100% largura no mobile | *(nada)* | 1 campo por linha |
| 50% largura no mobile | `cols="6"` | 2 campos por linha |
| 33% largura no mobile | `cols="4"` | 3 campos por linha |
| 25% largura no mobile | `cols="3"` | 4 campos por linha |

### Exemplo prático:
```vue
<!-- Padrão: 100% mobile, 25% desktop -->
<Input md="3" label="Nome" />

<!-- Customizado: 50% mobile, 25% desktop -->
<Input cols="6" md="3" label="CEP" />

<!-- Customizado: 33% mobile, 16% desktop -->
<Input cols="4" md="2" label="DDD" />
```

**Lembre-se:** Se você não passar `cols`, o padrão é `"12"` (100% no mobile) ✨
