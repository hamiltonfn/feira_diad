from flask import Flask, render_template_string, request, flash
import os

app = Flask(__name__)
app.secret_key = 'feira_secret_key_2025'

# Dados da feira
FEIRA_INFO = {
    'nome': 'Dia D da EPT - FEIRA DAS DISCIPLINAS TÉCNICAS',
    'data': '02 de Dezembro de 2025',
    'local': 'Escola CETI Bucar Neto',
    'horario': 'Terça: 08h às 17h'
}

def render_custom_template(template_content, **context):
    """Função personalizada para renderizar templates"""
    full_context = {
        'feira': FEIRA_INFO,
        **context
    }
    return render_template_string(template_content, **full_context)

# Template da página inicial (completo - sem herança)
INDEX_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ feira.nome }} - Página Inicial</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .hero-section {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            padding: 80px 0;
        }
        .info-card {
            margin-top: 30px;
        }
        .card {
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .navbar-brand {
            font-size: 1.5rem;
        }
        .hero-section h1 {
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .btn-success {
            background-color: #28a745;
            border-color: #28a745;
        }
        .btn-success:hover {
            background-color: #218838;
            border-color: #1e7e34;
        }
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .inspiration-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 30px 0;
        }
        .tool-link {
            text-decoration: none;
            color: inherit;
        }
        .tool-link:hover {
            color: inherit;
        }
        .tool-card {
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        .tool-card:hover {
            border-color: #28a745;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-success">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/">
                 {{ feira.nome }}
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/">Início</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/sobre">Sobre</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/contato">Contato</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section bg-primary text-white py-5">
        <div class="container text-center">
            <h1 class="display-4 fw-bold mb-3">{{ feira.nome }}</h1>
            <p class="lead mb-4">A criatividade é uma habilidade que pode ser aperfeiçoada e desenvolvida!</p>
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="info-card bg-white text-dark p-4 rounded shadow">
                        <div class="row text-center">
                            <div class="col-md-4 mb-3">
                                <i class="fas fa-calendar-alt fa-2x text-primary mb-2"></i>
                                <h5>Quando?</h5>
                                <p class="mb-0">{{ feira.data }}</p>
                            </div>
                            <div class="col-md-4 mb-3">
                                <i class="fas fa-map-marker-alt fa-2x text-primary mb-2"></i>
                                <h5>Onde?</h5>
                                <p class="mb-0">{{ feira.local }}</p>
                            </div>
                            <div class="col-md-4 mb-3">
                                <i class="fas fa-clock fa-2x text-primary mb-2"></i>
                                <h5>Horário</h5>
                                <p class="mb-0">{{ feira.horario }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Mensagem de Inspiração -->
    <section class="py-5">
        <div class="container">
            <div class="inspiration-box">
                <h3 class="mb-3">QUE AS FEIRAS SEJAM UM PERÍODO DE INSPIRAÇÃO PARA O PRÓXIMO ANO LETIVO</h3>
                <p class="lead mb-0">Descubra novas ferramentas, tecnologias e possibilidades que transformarão sua jornada educacional!</p>
            </div>
        </div>
    </section>

    <!-- Ferramentas de IA -->
    <section class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">FERRAMENTAS DE IA: UM MUNDO DE POSSIBILIDADES À SUA DISPOSIÇÃO!</h2>
            <div class="row">
                <div class="col-md-3 mb-4">
                    <a href="https://gamma.app/" target="_blank" class="tool-link">
                        <div class="card h-100 shadow text-center tool-card">
                            <div class="card-body">
                                <i class="fas fa-robot feature-icon text-primary"></i>
                                <h5 class="card-title">GAMMA APP</h5>
                                <p class="card-text">Criação de apresentações inteligentes com IA</p>
                                <small class="text-muted">Clique para acessar</small>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col-md-3 mb-4">
                    <a href="https://pt.akinator.com/" target="_blank" class="tool-link">
                        <div class="card h-100 shadow text-center tool-card">
                            <div class="card-body">
                                <i class="fas fa-magic feature-icon text-warning"></i>
                                <h5 class="card-title">AKINATOR</h5>
                                <p class="card-text">O gênio da web que adivinha o que você pensa</p>
                                <small class="text-muted">Clique para acessar</small>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col-md-3 mb-4">
                    <a href="https://luzia.com/" target="_blank" class="tool-link">
                        <div class="card h-100 shadow text-center tool-card">
                            <div class="card-body">
                                <i class="fas fa-comments feature-icon text-success"></i>
                                <h5 class="card-title">LuziA</h5>
                                <p class="card-text">Assistente virtual inteligente em português</p>
                                <small class="text-muted">Clique para acessar</small>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col-md-3 mb-4">
                    <a href="https://www.vidnoz.com/" target="_blank" class="tool-link">
                        <div class="card h-100 shadow text-center tool-card">
                            <div class="card-body">
                                <i class="fas fa-video feature-icon text-danger"></i>
                                <h5 class="card-title">Vidnoz</h5>
                                <p class="card-text">Criação de vídeos com tecnologia de IA</p>
                                <small class="text-muted">Clique para acessar</small>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            
            <!-- Quick Draw -->
            <div class="row justify-content-center mt-4">
                <div class="col-md-4">
                    <a href="https://quickdraw.withgoogle.com/" target="_blank" class="tool-link">
                        <div class="card shadow text-center tool-card">
                            <div class="card-header bg-info text-white">
                                <h5 class="mb-0">QUICK DRAW</h5>
                            </div>
                            <div class="card-body">
                                <p class="card-text">Desenhando com IA - A IA tenta adivinhar o que você desenha</p>
                                <small class="text-muted">Clique para acessar e desenhar</small>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Disciplinas Técnicas -->
    <section class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">COMPONENTES CURRICULARES - DESENVOLVIMENTO DE SISTEMAS</h2>
            <div class="row">
                <div class="col-md-6">
                    <ul class="list-group">
                        <li class="list-group-item"> TECNOLOGIAS E AMBIENTES VIRTUAIS DA APRENDIZAGEM</li>
                        <li class="list-group-item"> FUNDAMENTOS DA TECNOLOGIA DA INFORMAÇÃO</li>
                        <li class="list-group-item"> EDUCAÇÃO AMBIENTAL E SUSTENTABILIDADE</li>
                        <li class="list-group-item"> ARQUITETURA DE COMPUTADORES</li>
                        <li class="list-group-item"> FUNDAMENTOS DE BANCO DE DADOS</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <ul class="list-group">
                        <li class="list-group-item"> LÓGICA DE PROGRAMAÇÃO</li>
                        <li class="list-group-item"> FUNDAMENTOS DE REDES DE COMPUTADORES</li>
                        <li class="list-group-item"> INGLÊS TÉCNICO</li>
                        <li class="list-group-item"> MÉTODOS ÁGEIS DE DESENVOLVIMENTO</li>
                     
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Cursos Oferecidos -->
    <section class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">EM 2025 - ENSINO MÉDIO COM TÉCNICO INTEGRADO</h2>
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card shadow">
                        <div class="card-body text-center">
                            <h4 class="card-title mb-4">Cursos Técnicos Disponíveis</h4>
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="card bg-primary text-white mb-3">
                                        <div class="card-body">
                                            <h5>ADMINISTRAÇÃO</h5>
                                            <p class="mb-0">Com ênfase em empreendedorismo</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="card bg-success text-white">
                                        <div class="card-body">
                                            <h5>DESENVOLVIMENTO DE SISTEMAS</h5>
                                            <p class="mb-0">Formação em programação e tecnologia</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-5">
        <div class="container text-center">
            <h3 class="mb-4">Venha conhecer nossos projetos técnicos!</h3>
            <p class="lead mb-4">Uma oportunidade única de ver o talento e criatividade dos nossos alunos em ação.</p>
            <a href="/sobre" class="btn btn-success btn-lg me-3">Saiba Mais</a>
            <a href="/contato" class="btn btn-outline-success btn-lg">Entre em Contato</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white mt-5">
        <div class="container py-4">
            <div class="row">
                <div class="col-md-6">
                    <h5>{{ feira.nome }}</h5>
                    <p>{{ feira.data }}<br>
                    {{ feira.local }}<br>
                    {{ feira.horario }}</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p>&copy; 2025 {{ feira.nome }}. Todos os direitos reservados.</p>
                    <p class="mb-0">
                        <strong>Ferrira Infos</strong><br>
                        Rua Castro Alves, 1501, Floriano - PI<br>
                        Caixa d'Água | Redes Sociais: @cetibucarneto
                    </p>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# Template da página sobre
SOBRE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ feira.nome }} - Sobre</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .navbar-brand { font-size: 1.5rem; }
        .card { transition: transform 0.3s ease; }
        .card:hover { transform: translateY(-5px); }
        .seductec-box {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-success">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/"> {{ feira.nome }}</a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link" href="/">Início</a>
                <a class="nav-link active" href="/sobre">Sobre</a>
                <a class="nav-link" href="/contato">Contato</a>
            </div>
        </div>
    </nav>

    <div class="container py-5">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <h1 class="text-center mb-5">Sobre o Evento</h1>
                
                <div class="mb-5">
                    <h3><i class="fas fa-history me-2"></i>Nossa História</h3>
                    <p class="lead">O Dia "D" das Disciplinas Técnicas tem o objetivo de promover o conhecimento prático e oferecer uma experiência única para alunos e visitantes.</p>
                    <p>Desde 2024, reunimos os melhores conteúdos, alunos e professores para criar um evento que destaca nossas disciplinas técnicas e o talento dos estudantes.</p>
                </div>

                <!-- Programa SEDUCTEC -->
                <div class="seductec-box">
                    <h3><i class="fas fa-star me-2"></i>Programa SEDUCTEC</h3>
                    <p class="lead">Fortalecendo a Educação Profissional e Tecnológica no Piauí</p>
                    <p>Lançado em maio de 2023 com o objetivo de fortalecer a oferta de Educação Profissional e Tecnológica (EPT) no Ensino Médio e ajudar na formação de jovens qualificados para atendimento das atuais demandas do mundo do trabalho.</p>
                    <div class="mt-3">
                        <h5><i class="fas fa-clock me-2"></i>Carga Horária</h5>
                        <p>800 a 1.200 horas, distribuídas ao longo de 02 a 03 anos</p>
                    </div>
                </div>

                <div class="mb-5">
                    <h3><i class="fas fa-bullseye me-2"></i>Missão e Valores</h3>
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Nossa Missão</h5>
                            <p class="card-text">Promover e valorizar a Educação Profissional e Tecnológica, oferecendo excelência no ensino das disciplinas técnicas.</p>
                            
                            <h5 class="card-title mt-4">Nossos Valores</h5>
                            <ul>
                                <li>Excelência no ensino técnico</li>
                                <li>Inovação e criatividade</li>
                                <li>Compromisso com a qualidade</li>
                                <li>Desenvolvimento de competências profissionais</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="mb-5">
                    <h3><i class="fas fa-info-circle me-2"></i>Informações Importantes</h3>
                    <div class="card">
                        <div class="card-body">
                            <div class="row">
                                <div class="col-md-6">
                                    <p><strong><i class="fas fa-calendar me-2"></i>Data:</strong> {{ feira.data }}</p>
                                    <p><strong><i class="fas fa-map-marker-alt me-2"></i>Local:</strong> {{ feira.local }}</p>
                                    <p><strong><i class="fas fa-clock me-2"></i>Horário:</strong> {{ feira.horario }}</p>
                                </div>
                                <div class="col-md-6">
                                    <p><strong><i class="fas fa-users me-2"></i>Público:</strong> Aberto à comunidade</p>
                                    <p><strong><i class="fas fa-wheelchair me-2"></i>Acessibilidade:</strong> Totalmente acessível</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-dark text-white mt-5">
        <div class="container py-4">
            <div class="row">
                <div class="col-md-6">
                    <h5>{{ feira.nome }}</h5>
                    <p>{{ feira.data }}<br>{{ feira.local }}<br>{{ feira.horario }}</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p>&copy; 2025 {{ feira.nome }}</p>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# Template da página de contato
CONTATO_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ feira.nome }} - Contato</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .navbar-brand { font-size: 1.5rem; }
        .card { transition: transform 0.3s ease; }
        .card:hover { transform: translateY(-5px); }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-success">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/"> {{ feira.nome }}</a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link" href="/">Início</a>
                <a class="nav-link" href="/sobre">Sobre</a>
                <a class="nav-link active" href="/contato">Contato</a>
            </div>
        </div>
    </nav>

    <div class="container py-5">
        <div class="row">
            <div class="col-lg-8 mx-auto">
                <h1 class="text-center mb-5">Entre em Contato</h1>

                {% with messages = get_flashed_messages(with_categories=true) %}
                    {% if messages %}
                        {% for category, message in messages %}
                            <div class="alert alert-{{ 'success' if category == 'success' else 'danger' }} alert-dismissible fade show">
                                {{ message }}
                                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                            </div>
                        {% endfor %}
                    {% endif %}
                {% endwith %}

                <div class="row">
                    <div class="col-md-6 mb-4">
                        <div class="card h-100">
                            <div class="card-body">
                                <h4><i class="fas fa-info-circle me-2"></i>Informações de Contato</h4>
                                <div class="mb-3">
                                    <p><i class="fas fa-envelope me-2 text-primary"></i><strong>Email:</strong><br>escola@cetibucarneto.edu.br</p>
                                </div>
                                <div class="mb-3">
                                    <p><i class="fas fa-phone me-2 text-success"></i><strong>Telefone:</strong><br>(86) 9999-9999</p>
                                </div>
                                <div class="mb-3">
                                    <p><i class="fas fa-map-marker-alt me-2 text-danger"></i><strong>Endereço:</strong><br>Escola CETI Bucar Neto<br>Teresina - PI</p>
                                </div>
                                <div class="mb-3">
                                    <p><i class="fas fa-clock me-2 text-warning"></i><strong>Horário de Atendimento:</strong><br>Segunda a Sexta: 7h às 17h</p>
                                </div>
                                <div class="mb-3">
                                    <p><i class="fas fa-hashtag me-2 text-info"></i><strong>Redes Sociais:</strong><br>@cetibucarneto</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-body">
                                <h4><i class="fas fa-paper-plane me-2"></i>Formulário de Contato</h4>
                                <form method="POST">
                                    <div class="mb-3">
                                        <label for="nome" class="form-label">Nome Completo</label>
                                        <input type="text" class="form-control" id="nome" name="nome" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="email" class="form-label">Email</label>
                                        <input type="email" class="form-control" id="email" name="email" required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="telefone" class="form-label">Telefone</label>
                                        <input type="tel" class="form-control" id="telefone" name="telefone">
                                    </div>
                                    <div class="mb-3">
                                        <label for="assunto" class="form-label">Assunto</label>
                                        <select class="form-select" id="assunto" name="assunto">
                                            <option value="geral">Informações Gerais</option>
                                            <option value="visita">Agendar Visita</option>
                                            <option value="duvida">Dúvida sobre Cursos</option>
                                            <option value="outro">Outro</option>
                                        </select>
                                    </div>
                                    <div class="mb-3">
                                        <label for="mensagem" class="form-label">Mensagem</label>
                                        <textarea class="form-control" id="mensagem" name="mensagem" rows="4" required placeholder="Conte-nos como podemos ajudar..."></textarea>
                                    </div>
                                    <button type="submit" class="btn btn-success w-100">
                                        <i class="fas fa-paper-plane me-2"></i>Enviar Mensagem
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Mapa -->
                <div class="card mt-4">
                    <div class="card-body">
                        <h4><i class="fas fa-map me-2"></i>Localização</h4>
                        <div class="bg-light p-4 text-center rounded">
                            <i class="fas fa-map-marked-alt fa-3x text-muted mb-3"></i>
                            <p class="mb-2"><strong>Ferreira Infos</strong></p>
                            <p class="text-muted">Rua Castro Alves, 1501, Floriano - PI<br>Caixa d'Água</p>
                            <div class="mt-3">
                                <small class="text-muted">
                                    <i class="fas fa-bus me-1"></i>Ônibus: Linhas que passam próximas à escola
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-dark text-white mt-5">
        <div class="container py-4">
            <div class="row">
                <div class="col-md-6">
                    <h5>{{ feira.nome }}</h5>
                    <p>{{ feira.data }}<br>{{ feira.local }}<br>{{ feira.horario }}</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p>&copy; 2025 {{ feira.nome }}</p>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_custom_template(INDEX_TEMPLATE)

@app.route('/sobre')
def sobre():
    return render_custom_template(SOBRE_TEMPLATE)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form.get('telefone', '')
        assunto = request.form.get('assunto', 'geral')
        mensagem = request.form['mensagem']
        
        # Simulação de processamento do formulário
        print(f"Novo contato recebido:")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")
        print(f"Assunto: {assunto}")
        print(f"Mensagem: {mensagem}")
        
        flash(f'Obrigado {nome}! Sua mensagem foi enviada com sucesso. Entraremos em contato em breve!', 'success')
        
    return render_custom_template(CONTATO_TEMPLATE)

# Health check para plataformas de deploy
@app.route('/health')
def health_check():
    return 'OK'

if __name__ == '__main__':
    print("=" * 60)
    print("SITE DO DIA D DA EPT")
    print("=" * 60)
    print("Acesse: http://localhost:5000")
    print("Pressione Ctrl+C para parar o servidor")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)