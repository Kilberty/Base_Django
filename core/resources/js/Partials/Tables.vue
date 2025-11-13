<script setup>
import { computed, ref } from "vue";
import { BTable, BDropdown, BDropdownItem, BPagination } from "bootstrap-vue-next";

const props = defineProps({
  dados: {
    type: Array,
    default: () => [],
  },
  acoes: {
    type: Array,
    default: () => [],
  },
  perPage: {
    type: Number,
    default: 10,
  },
});

const currentPage = ref(1);

const colunas = computed(() => {
  if (!props.dados.length) return [];

  const dynamicFields = Object.keys(props.dados[0]).map((key) => ({
    key,
    label: key.charAt(0).toUpperCase() + key.slice(1),
    sortable: true,
  }));

  dynamicFields.push({
    key: "acoes",
    label: "Ações",
    thClass: "text-center",
    tdClass: "text-center",
    sortable: false,
  });

  return dynamicFields;
});

const totalRows = computed(() => props.dados.length);

const dadosPaginados = computed(() => {
  const start = (currentPage.value - 1) * props.perPage;
  const end = start + props.perPage;
  return props.dados.slice(start, end);
});
</script>

<template>
  <div class="bg-white rounded shadow-sm d-flex flex-column flex-grow-1">
    <div class="table-responsive flex-grow-1">
      <BTable striped hover :items="dadosPaginados" :fields="colunas" class="mb-0">
        <template #cell(acoes)="{ item }">
          <BDropdown
            size="sm"
            boundary="viewport"
            text="Ações"
            variant="outline-dark"
            placement="right"
            menu-class="dropdown-menu-end"
          >
            <BDropdownItem
              v-for="(acao, index) in acoes"
              :key="index"
              @click="acao.action(item)"
            >
              {{ acao.label }}
            </BDropdownItem>
          </BDropdown>
        </template>

        <template #empty>
          <div class="text-center text-muted p-4">
            Nenhum registro encontrado.
          </div>
        </template>
      </BTable>
    </div>
    
    <!-- Paginador -->
    <div v-if="totalRows > 0" class="p-3 border-top mt-auto">
      <div class="d-flex justify-content-between align-items-center">
        <small class="text-muted">
          Mostrando {{ (currentPage - 1) * perPage + 1 }} a {{ Math.min(currentPage * perPage, totalRows) }} de {{ totalRows }} registros
        </small>
        <div class="ms-auto">
          <BPagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            size="sm"
            :limit="7"
            first-text="‹‹"
            last-text="››"
            prev-text="‹"
            next-text="›"
          />
        </div>
      </div>
    </div>
  </div>
</template>
