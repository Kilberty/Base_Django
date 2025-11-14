# Sistema de Filtros - Backend Django

## Como funciona o filtro

### 1. Frontend (Vue.js + Inertia)
```javascript
// Usuarios.vue
const formFiltro = useForm({
  nome: ""
});

function handleFilter() {
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
```

**O que acontece:**
- Usuário digita "João" no campo de filtro
- Usuário aperta Enter ou clica em "Pesquisar"
- Inertia faz uma requisição GET para: `/usuarios/?nome=João`
- Backend processa e retorna os dados filtrados

### 2. Backend (Django)
```python
def index(request):
    # Pega o parâmetro 'nome' da URL
    filtro_nome = request.GET.get('nome', '').strip()
    
    # Inicia a query
    usuarios = Usuario.objects.all()
    
    # Aplica filtro se existir
    if filtro_nome:
        usuarios = usuarios.filter(nome__icontains=filtro_nome)
    
    # Retorna resultados
    usuarios = usuarios.values('id', 'nome', 'email').order_by('id')
```

## Tipos de filtros Django

### Filtros básicos
```python
# Exato (case sensitive)
usuarios.filter(nome__exact='João')

# Exato (case insensitive)
usuarios.filter(nome__iexact='joão')

# Contém (case sensitive)
usuarios.filter(nome__contains='João')

# Contém (case insensitive) - RECOMENDADO PARA BUSCA
usuarios.filter(nome__icontains='joão')

# Começa com
usuarios.filter(nome__startswith='João')

# Termina com
usuarios.filter(nome__endswith='Silva')
```

### Filtros numéricos
```python
# Maior que
usuarios.filter(idade__gt=18)

# Maior ou igual
usuarios.filter(idade__gte=18)

# Menor que
usuarios.filter(idade__lt=60)

# Menor ou igual
usuarios.filter(idade__lte=60)

# Entre valores
usuarios.filter(idade__range=(18, 60))
```

### Filtros de data
```python
# Data exata
usuarios.filter(data_cadastro__date='2025-11-14')

# Ano
usuarios.filter(data_cadastro__year=2025)

# Mês
usuarios.filter(data_cadastro__month=11)

# Dia
usuarios.filter(data_cadastro__day=14)

# Entre datas
from datetime import datetime
data_inicio = datetime(2025, 1, 1)
data_fim = datetime(2025, 12, 31)
usuarios.filter(data_cadastro__range=(data_inicio, data_fim))
```

### Filtros de relacionamento
```python
# Filtrar por campo de FK (Foreign Key)
usuarios.filter(empresa__nome='Empresa XYZ')

# Filtrar por múltiplos relacionamentos
usuarios.filter(empresa__cidade='São Paulo')
```

## Exemplo completo com múltiplos filtros

### Frontend
```javascript
// Usuarios.vue
const formFiltro = useForm({
  nome: "",
  email: "",
  status: "",
  data_inicio: "",
  data_fim: ""
});

function handleFilter() {
  formFiltro.get('/usuarios/', {
    preserveState: true,
    preserveScroll: true,
  });
}
```

```vue
<FilterForm @submit="handleFilter">
  <template #filters>
    <div class="col-12 col-md-3">
      <label class="form-label">Nome</label>
      <input type="text" class="form-control" v-model="formFiltro.nome" />
    </div>
    
    <div class="col-12 col-md-3">
      <label class="form-label">Email</label>
      <input type="text" class="form-control" v-model="formFiltro.email" />
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
      <input type="date" class="form-control" v-model="formFiltro.data_inicio" />
    </div>
    
    <div class="col-12 col-md-2">
      <label class="form-label">Data Fim</label>
      <input type="date" class="form-control" v-model="formFiltro.data_fim" />
    </div>
  </template>
</FilterForm>
```

### Backend
```python
def index(request):
    usuario_logado = request.user
    
    # Pega todos os parâmetros de filtro
    filtro_nome = request.GET.get('nome', '').strip()
    filtro_email = request.GET.get('email', '').strip()
    filtro_status = request.GET.get('status', '').strip()
    filtro_data_inicio = request.GET.get('data_inicio', '').strip()
    filtro_data_fim = request.GET.get('data_fim', '').strip()
    
    # Inicia a query base
    usuarios = Usuario.objects.all()
    
    # Aplica cada filtro se existir
    if filtro_nome:
        usuarios = usuarios.filter(nome__icontains=filtro_nome)
    
    if filtro_email:
        usuarios = usuarios.filter(email__icontains=filtro_email)
    
    if filtro_status:
        usuarios = usuarios.filter(status=filtro_status)
    
    if filtro_data_inicio:
        from datetime import datetime
        data_inicio = datetime.strptime(filtro_data_inicio, '%Y-%m-%d')
        usuarios = usuarios.filter(data_cadastro__gte=data_inicio)
    
    if filtro_data_fim:
        from datetime import datetime
        data_fim = datetime.strptime(filtro_data_fim, '%Y-%m-%d')
        usuarios = usuarios.filter(data_cadastro__lte=data_fim)
    
    # Ordena e seleciona campos
    usuarios = usuarios.values('id', 'nome', 'email', 'status', 'data_cadastro').order_by('id')
    
    props = {
        "usuario": {
            "id": usuario_logado.id if usuario_logado.is_authenticated else None,
            "nome": getattr(usuario_logado, "nome", ""),
            "email": getattr(usuario_logado, "email", "")
        },
        "usuarios_cadastrados": list(usuarios)
    }
    return render(request, "Usuarios", props)
```

## Dicas importantes

1. **Sempre use `.strip()`** para remover espaços em branco
2. **Use `icontains` para buscas de texto** (ignora maiúsculas/minúsculas)
3. **Valide datas** antes de usar em filtros
4. **Use `values()` para otimizar queries** (seleciona apenas campos necessários)
5. **Sempre ordene os resultados** com `order_by()`
6. **Use `preserveState: true`** no Inertia para manter estado da página
7. **Use `preserveScroll: true`** para não voltar ao topo da página

## Testando filtros

### No navegador
Acesse manualmente: `http://localhost:8000/usuarios/?nome=João`

### No console do navegador
```javascript
// Ver a URL atual com filtros
console.log(window.location.href)

// Ver os parâmetros do formFiltro
console.log(formFiltro.data())
```

### No Django shell
```python
python manage.py shell

from usuarios.models import Usuario

# Testar filtro
usuarios = Usuario.objects.filter(nome__icontains='joão')
print(list(usuarios.values('id', 'nome', 'email')))
```
