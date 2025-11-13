<script setup>
import { defineProps, defineEmits } from "vue";
import { BCol,BFormGroup,BFormInput} from "bootstrap-vue-next";
defineProps({
  id: String,
  name: String,
  label: String,
  cols:String,
  type:String,
  modelValue: [String, Number],
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
      <BCol :cols="cols" v-bind="$attrs"> 
        <BFormGroup :label="label">
          <BFormInput
            :id="id"
            :name="name"
            :value="modelValue"
            :type="type"
            @input="(event) => emit('update:modelValue', event.target.value)"
          />
        </BFormGroup>
      </BCol>
</template>
<style>
</style>