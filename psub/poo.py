class Canal:
    def __init__(self, nome, desc, inscritos):
        self.nome = nome
        self.desc = desc
        self.inscritos = inscritos
        self.videos = []
        self.playlist = []

    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print("Video ja foi postado")
            return 
        else:
            self.videos.append(video)

    def playlists(self, playlist):
        self.playlist.append(playlist)

    def exibir_playlist(self):
        for video in self.playlist:
            print(video)

# print(canal_guanabara.inscritos)
# canal_guanabara.inscrever(500)
# print(canal_guanabara.inscritos)

class CanalEmpresarial(Canal):
    def __init__(self, nome, desc, inscritos):
        super().__init__(nome, desc, inscritos)
        self._equipe = [] # Apenas de canal empresarial

    @property # getter
    def equipe(self):
        return self._equipe
    
    def adicionar_membro(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print("Esse membro já está na equipe")

    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print("Esse membro não está na equipe")

class Video:
    def __init__(self, titulo, descricao, data_publicacao):
        self.titulo = titulo
        self.descricao = descricao

        self.visualizacoes = 0
        self.likes = 0
        self.deslikes = 0
        self. comentarios = []
        self.data_publicacao = data_publicacao

    def __repr__(self):
        return f"<{self.titulo}>"

    def assistir(self):
        self.visualizacoes += 1

    def gostei(self):
        self.likes += 1

    def nao_gostei(self):
        self.deslikes += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def data_publicar(self):
        return self.data_publicacao 

    def info(self):
        print(f"""Título: {self.titulo}
Descrição: {self.descricao}
Data da postagem: {self.data_publicacao}
{self.visualizacoes} Visualizações
{self.likes} Likes {self.deslikes} Deslikes
{self.comentarios}\n""")
        

class Playlist:
    def __init__(self, titulo):
        self.titulo = titulo
        self.videos = []

    def inserir_video(self, video):
        if video in self.videos:
            print("Este video já está na playlist")
            return
        else:
            self.videos.append(video)

    def remover_video(self, video):
        if video not in self.videos:
            print("Este video não existe na playlist")
            return
        else:
            self.videos.remove(video)

    def informacoes(self):
        print(f"""Titulo da playlist: {self.titulo}
Videos na playlist: {self.videos}\n""")
        
video_poo = Video("Video Legal", "Aprenda agora", "23/06/2026")

canal_duolingo = CanalEmpresarial('Duolingo', 'Inglês', 200000)
canal_guanabara = Canal('Curso em video', 'Paixao por ensinar', 2500000)
canal_guanabara.postar(video_poo)
playlist_python = Playlist("Python")
canal_guanabara.playlists(playlist_python)

playlist_python.inserir_video(video_poo)
playlist_python.informacoes()

print(canal_guanabara.playlist)