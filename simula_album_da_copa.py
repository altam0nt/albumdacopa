import numpy as np
import pandas as pd


def simula_album(total_figs, pacote_figs):
    pop_figs = pd.Series(np.ones(total_figs), index=range(1, total_figs + 1))
    figs = pd.Series(np.zeros(total_figs), index=pop_figs.index)

    while ~figs.all():
        pacote = pop_figs.sample(n=pacote_figs)
        figs = figs.add(pacote, fill_value=0)

    return figs


def n_pacotes(figs):
    return figs.sum() / 5


def custo_pacotes(figs, preco_pacote):
    return n_pacotes(figs) * preco_pacote


def repetidas(figs):
    reps = figs[figs > 1]
    return reps.sum() - reps.size


if __name__=="__main__":
    total_figs = 682
    pacote_figs = 5
    preco_pacote = 2.00

    albuns = pd.DataFrame(columns=["Pacotes", "Custo", "Repetidas"])
    figs = pd.Series(np.zeros(total_figs), index=range(1, total_figs + 1)) 
    
    for i in range(1, 1001):
        album = simula_album(total_figs, pacote_figs)
        
        albuns.loc[i] = [
            n_pacotes(album),
            custo_pacotes(album, preco_pacote),
            repetidas(album)
        ]

        figs = figs.add(album)

    albuns.to_csv('simulacao_albuns_da_copa.csv')
    figs.to_csv('figurinhas_total.csv')

        

