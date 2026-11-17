from pathlib import Path
import sqlite3

NOME_BANCO = Path(__file__).resolve().parent / "cadastro.db"

with sqlite3.connect(NOME_BANCO) as db:
    pass

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS pessoas(cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL);")
            return True
    except sqlite3.Error as erro:
        print(f"Falha na criação do banco: {erro}")
        return False
    
def cadastro_em_massa():
    cad_pessoas = [
        ("1","katia", "1.84"),
        ("2","leandro", "1.63"),
        ("3","januario", "2.02"),
        ("4","lindomar", "1.72"),
    ]
    
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.executemany("INSERT INTO pessoas(cod, nome, altura) VALUES (?, ?, ?)", cad_pessoas)
        
    except sqlite3.Error as erro:
        print("\n[ERRO] Falha ao criar cadastro em massa..")
        
def Cadastrar_Pessoa() -> bool:
    
    print("\n ==== NOVO CADASTRO DE PESSOA ==== ")
    # leitura e Validacao de dados
    val_nome = input("Nome: ").strip()
    if not val_nome:
        print("[ERRO] o nome é um campo obrigatorio!")
        return False
    val_altura = input("Altura (metros): ").strip().replace(",",".")
    if not val_altura:
        print("[ERRO] A Altrura é um campo obrigatorio!")
        return False
    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.0:
            print("[ERRO] Valor incoerente para Altura.")
            return False
    except ValueError:
        print("[ERRO] A Altura precisa ser um numero.")
    
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)", (val_nome, val_altura))
            print(f"Cadastro de {val_nome} realizado com sucesso!")
            return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha no cadastro do banco: {erro}")
        return False
        
def Listar_Pessoas() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas ORDER BY nome;")
            primeiro = cur.fetchone()
            if not primeiro:
                print("[AVISO] Nenhuma pessoa foi cadastrada ate agora.")
                return True
            print(f"\n" + "=" * 45)
            print(f"{'CÓD':<8} {'NOME':<18} {'ALTURA':>15}")
            print(f"-" * 45)
            
            vcod, vnome, valtura = primeiro
            print(f"{vcod:<8} {vnome:<18} {valtura:>15}m")
            
            for vcod, vnome, valtura in cur:
                print(f"{vcod:<8} {vnome:<18} {valtura:>15}m")
                
            print(f"\n" + "=" * 45)
            return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao acessar o banco: {erro}")
        return False

def Buscar_por_nome() -> bool:
    print("\n --- BUSCA DE PESSOA POR NOME --- " )
    termo = input("Digite o nome (ou parte dele) para buscar: ")
    if not termo:
        print(f"[AVISO] Nenhum termo foi informado ")
        return True
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas WHERE nome LIKE ? ORDER BY nome;", (f"%{termo}%",))
            
            primeiro = cur.fetchone()
            if not primeiro:
                 print(f"[AVISO] Nenhuma pessoa foi encontrada com '{termo}'.")
                 return True
            print(f"\n" + "=" * 45)
            print(f"{'CÓD':<8} {'NOME':<18} {'ALTURA':>15}")
            print(f"-" * 45)
             
            vcod, vnome, valtura = primeiro
            print(f"{vcod:<8} {vnome:<18} {valtura:>15}m")
             
            for vcod, vnome, valtura in cur:
                print(f"{vcod:<8} {vnome:<18} {valtura:>15}m")
                 
            print(f"\n" + "=" * 45)
            return True           
    except sqlite3.Error as erro:
        print(f"[ERRO] Falaha ao buscar")
        return False

def Atualizar_Pessoa() -> bool:
   pass

def Excluir_Pessoa() -> bool:
  pass