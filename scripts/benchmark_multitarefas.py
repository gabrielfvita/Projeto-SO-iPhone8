import multiprocessing as mp
import hashlib
import tempfile
import zlib
import time
import os
import sys

DURACAO = 120

CENARIOS = {
    "leve": ["cpu", "compressao"],
    "medio": ["cpu", "compressao", "disco"],
    "pesado": [
        "cpu", "cpu",
        "compressao", "compressao",
        "disco", "disco"
    ]
}

def cpu(fim):
    dados = b"A" * (1024 * 1024)
    operacoes = 0

    while time.monotonic() < fim:
        hashlib.sha256(dados).digest()
        operacoes += 1

    print("CPU:", operacoes, "hashes", flush=True)

def compressao(fim):
    dados = os.urandom(512 * 1024)
    operacoes = 0

    while time.monotonic() < fim:
        comprimido = zlib.compress(dados, 1)
        zlib.decompress(comprimido)
        operacoes += 1

    print("Compressao:", operacoes, "ciclos", flush=True)

def disco(fim):
    dados = os.urandom(1024 * 1024)
    operacoes = 0

    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, "teste.bin")

        while time.monotonic() < fim:
            with open(caminho, "wb") as arquivo:
                arquivo.write(dados)

            with open(caminho, "rb") as arquivo:
                arquivo.read()

            operacoes += 1

    print("Disco:", operacoes, "ciclos", flush=True)

FUNCOES = {
    "cpu": cpu,
    "compressao": compressao,
    "disco": disco
}

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in CENARIOS:
        print("Uso: python3 benchmark_multitarefas.py leve|medio|pesado")
        return

    nivel = sys.argv[1]
    tarefas = CENARIOS[nivel]

    print("Cenario:", nivel)
    print("Tarefas:", ", ".join(tarefas))
    print("Duracao:", DURACAO, "segundos")
    print("Iniciando em 5 segundos...", flush=True)

    time.sleep(5)
    fim = time.monotonic() + DURACAO
    processos = []

    try:
        for tarefa in tarefas:
            p = mp.Process(
                target=FUNCOES[tarefa],
                args=(fim,)
            )
            p.start()
            processos.append(p)

        print("BENCHMARK INICIADO!", flush=True)

        for p in processos:
            p.join()

    except KeyboardInterrupt:
        print("Interrompendo...", flush=True)

    finally:
        for p in processos:
            if p.is_alive():
                p.terminate()
        for p in processos:
            p.join()

        print("Benchmark encerrado.", flush=True)

if __name__ == "__main__":
    main()
