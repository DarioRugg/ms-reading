#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pymzml


def main():
    """
    This function shows how to plot a simple spectrum. It can be directly
    plotted via this script or using the python console.

    usage:

        ./plot_spectrum.py

    """

    example_file = os.path.join(
        "../data/TQ8_201023SJ01_0103.mzML"
    )
    run = pymzml.run.Reader(example_file)
    p = pymzml.plot.Factory()
    for spec in list(run)[6000:6003]:
        p.new_plot()
        # p.add(cumulative_spec.peaks("raw"), color=(0, 0, 0), style="sticks", name="peaks")
        p.add(list(zip(spec.mz, spec.i)), color=(0, 0, 0), style="sticks", name="peaks")
        filename = "example_plot_{0}_{1}.html".format(
            os.path.basename(example_file), spec.ID
        )
        p.save(filename=filename)
        print("Plotted file: {0}".format(filename))
        break


if __name__ == "__main__":
    main()