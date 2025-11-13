<!-- todo template de página consiste em três etapas
 
<script setup > </script>
<template></template>
<style></style>


no script você vai colocar as funções do frontend, a parte lógica
no template você coloca a parte visual
no style você edita a parte visual, como por exemplo, muda uma cor, aumenta um tamanho de letra e etc


veja abaixo que sempre que você for usar um componente que não foi definido na página, você tem que importar de onde ele foi definido,
ou seja, sempre que você for usar um componente reutilizável, você tem que adicionar o import dele.

-->
<script setup>
import Auth from "../Layout/Auth.vue";
import Tables from "../Partials/Tables.vue";
import Input from "../Components/Input.vue";
import InputError from "../Components/InputError.vue";
import { useForm } from "@inertiajs/vue3";
import { BForm, BRow } from "bootstrap-vue-next";
//props são as informações da API para que essas informações sejam usadas na página, elas tem que ser definidas como props antes
const props = defineProps({
  //usuario é a prop onde você pega as informações do usuário logado
  usuario: { type: Object, default: () => ({}) },
  //usuarios_cadastrados é a prop onde você pega a lista completa de usuários cadastrados, por isso é um array
  // lembrando que um array pode ser uma lista de objetos, é um caso comum.
  usuarios_cadastrados: { type: Array, default: () => [] },
  // estado é a prop que vai dizer se o modal de cadastro está aberto ou fechado
  estado: Boolean
});
//const emit é uma constante(valor da constante é imutável depois de definido)
//aqui definimos que emit vai atualizar o valor de "estado"
const emit = defineEmits(["update:estado"]);

//const form vai ser uma instancia de useform, trate isso como um apelido para useform
//dentro do form, perceba que existem informações como "nome","email"
//você vai definir uma dessa para cada informação que for necessária para o cadastro, o backend vai pegar as informações a partir daqui
const form = useForm({
  nome: "",
  email: "",
  password: "",
  password2: ""
});

//Isso aqui é um exemplo de ações que vão ser passadas nos botões de editar na tabela
// a parte de criar as ações é manual realmente e exige algum conhecimento
const acoes = [
  { label: "Editar Funcionário", action: item => console.log("Editando:", item.nome) },
  { label: "Excluir Funcionário", action: item => console.log("Excluindo:", item.nome) }
];



//essa é a função de salvar, vai ser a função que vai ser passada para o botão de salvar no modal, é aqui que ele se comunica com o backend
//basicamente essa função será a mesma para todos os modais, apenas alterando a rota
// a rota atual é /usuarios/cadastrar, caso fosse um cadastro de empresa por exemplo poderia ser /empresa/cadastrar
function handleSave(event) {
  if (event) event.preventDefault();
  
  form.post('/usuarios/cadastrar/',{
    preserveScroll: true,
    onSuccess:()=>{
     emit("update:estado", false);
     form.reset()
    },
    })
}
</script>

<template>
  <!-- 
   titulo = Define o titulo da página de cadastros, sempre aparecerá no topo do lado esquerdo
   :nome = Mostra o nome do usuário que logou no sistema, toda tela pós autenticação terá essa informação
   :cadastro = define se os botões de cadastro irão aparecer ou nao
   :info = define se os botões da janela de informações vão aparecer ou não
   
   diferença de cadastro e info :

   Cadastro é a tela que o usuário vai abrir ANTES de chegar na tela de informação, é como essa tela aqui mostrada de exemplo
   Info é a tela em que o usuário chega APÓS apertar em editar algo no botão de ações

   o botão de cadastro ADICIONA e o botão de info SALVA as informações, sendo assim, rotas diferentes e rotinas diferentes por isso a separação
  
   :estado = passa a informação para o sistema se o modal(Janelinha com as informações de cadastro) deve continuar aberto ou se deve fechar

   continuar aberto = cadastro falhou, precisa de correção nas informações
   fechar o modal = cadastro foi concluido, vai fechar e atualizar as informações no sistema

   titulo_modal = todo modal tem um titulo que vai explicar para o usuário qual a sua função, você define o titulo nessa props
  
   :modalOnSave = Passa a função que salva as informações cadastradas, assim você nao precisa recriar toda a base do modal em todas as telas
   é só passar a função para o modal, e é por isso que existe a diferença entre info e cadastro
   
   em info NÃO VAI ABRIR MODAL, ele vai salvar diretamente quando apertar salvar, por que o botão é diferente

   a tela de info não foi criada na base, pois a base só tem usuários e usuários não precisam de uma tela completa de info.
  
  
  
  
  -->
  <Auth
    titulo="Usuários"
    :nome="props.usuario.nome" 
    :cadastro="true"
    :info="false"
    :estado="props.estado"
    titulo_modal="Cadastrar Usuário"
    :modalOnSave="handleSave"
  >
    
  <!-- Essa é a unica parte "manual" do frontend, é só seguir o exemplo desse para telas de cadastro -->
  <template #modal-body>
      <BForm>
        <BRow>
          <div class="col-12">
            <!--
              name = nome do componente
              id = repita o name
              type = tipo do input, por exemplo password vai deixar a senha criptografada visualmente, date vai ser um campo de data
              cols = tamanho do campo, por padrão da forma que estou usando a largura da tela(ou componente) se divide em 12 partes iguais
              no caso se eu defino um input cols="12" quer dizer que eu quero que esse input ocupe toda a linha
              label = nome que vai ficar acima do input
              v-model = nome da variavel que você definiu no form, por exemplo se você quer que aquele input pegue a informação de nome do form
              você coloca form.nome 
            
            -->
            <Input name="nome" type="text" id="nome" cols="12" label="Nome" v-model="form.nome" />
            <InputError :message="form.errors.nome ? form.errors.nome[0] : null"/>
          </div>
        </BRow>
        <BRow class="mt-3 mb-3">
          <div class="col-6">
            <Input name="email" v-model="form.email" id="email" type="email" cols="12" label="Email" />
            <InputError :message="form.errors.email ? form.errors.email[0] : null"/>
          </div>
          <div class="col-3">
            <Input name="password" id="password" v-model="form.password" type="password" label="Senha" cols="12" />
            <InputError :message="form.errors.password ? form.errors.password[0] : null"/>
          </div>
          <div class="col-3">
            <Input name="cpassword" id="cpassword" v-model="form.password2" type="password" label="Confirme a senha" cols="12" />
            <InputError :message="form.errors.password2 ? form.errors.password2[0] : null"/>
          </div>
        </BRow>
        <!-- Erro geral (ex: senhas não coincidem) -->
        <InputError v-if="form.errors.__all__" :message="form.errors.__all__[0]" className="text-center"/>
      </BForm>
    </template>
    
    <!--A tabela toda será gerada na linha abaixo, só é preciso repetir em outras janelas o nome da props com os dados-->
    <Tables :dados="props.usuarios_cadastrados" :acoes="acoes" />
  </Auth>
</template>