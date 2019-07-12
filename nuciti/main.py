from dataclasses import dataclass
from hashlib import blake2b
from pathlib import Path

import numpy as np
import pandas as pd
from austen import Logger
from networkx import Graph

import data
import ga

LOGS = Path('logs')


@dataclass(init=True)
class Batch():
    graph: Graph
    params: ga.Params


def __batch_as_hash(params):
    encoded = str(params).encode('utf-8')
    return blake2b(encoded, digest_size=4).hexdigest()


def main():
    graph = data.generate()

    batches = [
        Batch(
            graph,
            ga.Params(100, 100, 0.4, 0.5, 0.1)
        )
    ]

    for batch in batches:
        graph = batch.graph
        params = batch.params

        params_hash = __batch_as_hash(params)

        logs_dir = LOGS.joinpath(params_hash)

        with Logger(logs_dir) as logger:
            ga_stats = ga.run(graph, params)

            worst = []
            mean = []
            best = []

            for epoch_stats in ga_stats:
                worst.append(np.min(epoch_stats.scores))
                mean.append(np.mean(epoch_stats.scores))
                best.append(np.max(epoch_stats.scores))

            summary = {}
            summary['worst'] = worst
            summary['mean'] = mean
            summary['best'] = best

            data_frame = pd.DataFrame.from_dict(summary)
            logger.save_csv(data_frame, 'summary')





if __name__ == "__main__":
    main()
