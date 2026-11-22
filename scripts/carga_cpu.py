import multiprocessing as mp
import hashlib
import time
import sys

DURACAO = 120
PROCESSOS = 12

NIVEIS = {
    "leve": 0.20,
    "media": 0.60,
    "pesada": 1.00
}

def trabalhador(intensidade, fim):
    dados = b"A" * (1024 * 1024)
    periodo = 0.1

    while time.monotonic() < fim:
        inicio = time.monotonic()

        while (
            time.monotonic() - inicio < periodo * intensidade
            and time.monotonic() < fim
        ):
            hashlib.sha256(dados).digest()

        pausa = periodo - (time.monotonic() - inicio)

        if pausa > 0:
            time.sleep(pausa)

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in NIVEIS:
        print("Uso: python3 carga_cpu.py leve|media|pesada")
        return

    nivel = sys.argv[1]
    intensidade = NIVEIS[nivel]

    print("Nivel:", nivel, flush=True)
    print("Processos:", PROCESSOS, flush=True)
    print("Intensidade por processo:", intensidade * 100, "%", flush=True)
    print("Duracao:", DURACAO, "segundos", flush=True)

    print("Iniciando em 5 segundos...", flush=True)
    time.sleep(5)

    fim = time.monotonic() + DURACAO
    processos = []

    try:
        for _ in range(PROCESSOS):
            p = mp.Process(
                target=trabalhador,
                args=(intensidade, fim)
            )
            p.start()
            processos.append(p)

        print("CARGA INICIADA!", flush=True)

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

        print("Teste encerrado.", flush=True)

if __name__ == "__main__":
    main()
