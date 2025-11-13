import { createApp, h } from "vue";
import { createInertiaApp } from "@inertiajs/vue3";

// Você só precisa das declarações de importação de CSS aqui
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";

// Função alternativa ao resolvePageComponent
function resolvePageComponent(name, pages) {
  const importPage = pages[`./Pages/${name}.vue`];
  if (!importPage) throw new Error(`Página não encontrada: ${name}`);
  return importPage();
}

createInertiaApp({
  resolve: (name) => resolvePageComponent(name, import.meta.glob("./Pages/**/*.vue")),
  setup({ el, App, props, plugin }) {
    const app = createApp({ render: () => h(App, props) });
    app.use(plugin);
    app.mount(el);
  },
});