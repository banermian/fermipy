#!/usr/bin/env python
from setuptools import setup, find_packages
from fermipy.version import get_git_version

setup(
    name='fermipy',
    version=get_git_version(),
    author='The Fermipy developers',
    author_email='fermipy.developers@gmail.com',
    description='A Python package for analysis of Fermi-LAT data',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/fermiPy/fermipy",
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Development Status :: 4 - Beta',
    ],
    scripts=[],
    entry_points={'console_scripts': [
        'fermipy-dispatch = fermipy.scripts.dispatch:main',
        'fermipy-clone-configs = fermipy.scripts.clone_configs:main',
        'fermipy-collect-sources = fermipy.scripts.collect_sources:main',
        'fermipy-cluster-sources = fermipy.scripts.cluster_sources:main',
        'fermipy-flux-sensitivity = fermipy.scripts.flux_sensitivity:main',
        'fermipy-intensity-map = fermipy.scripts.intensity_map:main',
        'fermipy-run-tempo = fermipy.scripts.run_tempo:main',
        'fermipy-healview = fermipy.scripts.HEALview:main',
        'fermipy-wcsview = fermipy.scripts.WCSview:main',
        'fermipy-gethdutype = fermipy.scripts.gethdutype:main',
        'fermipy-select = fermipy.scripts.select_data:main',
        'fermipy-preprocess = fermipy.scripts.preprocess_data:main',
        'fermipy-astroserver = fermipy.scripts.astroserver:main',
        'fermipy-validate = fermipy.scripts.validate:main',
        'fermipy-merit-skimmer = fermipy.scripts.merit_skimmer:main',
        'fermipy-merit-response = fermipy.scripts.merit_response:main',
        'fermipy-quick-analysis = fermipy.scripts.quickanalysis:main',
        'fermipy-coadd = fermipy.scripts.coadd:main',
        'fermipy-vstack = fermipy.scripts.vstack_images:main',
        'fermipy-gather-srcmaps = fermipy.scripts.gather_srcmaps:main',
        'fermipy-gtexcube2-sg = fermipy.diffuse.job_library:Gtexpcube2_SG.main',
        'fermipy-gtltsum-sg = fermipy.diffuse.job_library:Gtltsum_sg.main',
        'fermipy-sum-ring-gasmaps-sg = fermipy.diffuse.job_library:SumRings_SG.main',
        'fermipy-vstack-diffuse-sg = fermipy.diffuse.job_library:Vstack_SG.main',
        'fermipy-gather-srcmaps-sg = fermipy.diffuse.job_library:GatherSrcmaps_SG.main',
        'fermipy-healview-sg = fermipy.diffuse.job_library:Healview_SG.main',
        'fermipy-gtexphpsun-sg = fermipy.diffuse.solar:Gtexphpsun_SG.main',
        'fermipy-gtsuntemp-sg = fermipy.diffuse.solar:Gtsuntemp_SG.main',
        'fermipy-coadd-split = fermipy.diffuse.gt_coadd_split:CoaddSplit.main',
        'fermipy-coadd-split-sg = fermipy.diffuse.gt_coadd_split:CoaddSplit_SG.main',
        'fermipy-srcmaps-catalog = fermipy.diffuse.gt_srcmaps_catalog:GtSrcmapsCatalog.main',
        'fermipy-srcmaps-catalog-sg = fermipy.diffuse.gt_srcmaps_catalog:SrcmapsCatalog_SG.main',
        'fermipy-srcmaps-diffuse = fermipy.diffuse.gt_srcmap_partial:GtSrcmapsDiffuse.main',
        'fermipy-srcmaps-diffuse-sg = fermipy.diffuse.gt_srcmap_partial:SrcmapsDiffuse_SG.main',
        'fermipy-merge-srcmaps = fermipy.diffuse.gt_merge_srcmaps:GtMergeSourceMaps.main',
        'fermipy-merge-srcmaps-sg = fermipy.diffuse.gt_merge_srcmaps:MergeSourceMaps_SG.main',
        'fermipy-init-model = fermipy.diffuse.gt_assemble_model:GtInitModel.main',
        'fermipy-assemble-model = fermipy.diffuse.gt_assemble_model:GtAssembleModel.main',
        'fermipy-assemble-model-sg = fermipy.diffuse.gt_assemble_model:AssembleModel_SG.main',
        'fermipy-residual-cr = fermipy.diffuse.residual_cr:ResidualCR.main',
        'fermipy-residual-cr-sg = fermipy.diffuse.residual_cr:ResidualCR_SG.main',
        'fermipy-split-and-bin = fermipy.diffuse.gt_split_and_bin:SplitAndBin.main',
        'fermipy-split-and-bin-sg = fermipy.diffuse.gt_split_and_bin:SplitAndBin_SG.main',
        'fermipy-split-and-bin-chain = fermipy.diffuse.gt_split_and_bin:SplitAndBinChain.main',
        'fermipy-split-and-mktime = fermipy.diffuse.gt_split_and_mktime:SplitAndMktime.main',
        'fermipy-split-and-mktime-sg = fermipy.diffuse.gt_split_and_mktime:SplitAndMktime_SG.main',
        'fermipy-split-and-mktime-chain = fermipy.diffuse.gt_split_and_mktime:SplitAndMktimeChain.main',
        'fermipy-residual-cr-chain = fermipy.diffuse.residual_cr:ResidualCRChain.main',
        'fermipy-sunmoon-chain = fermipy.diffuse.solar:SunMoonChain.main',
        'fermipy-catalog-comp-chain = fermipy.diffuse.catalog_src_manager:CatalogCompChain.main',
        'fermipy-diffuse-comp-chain = fermipy.diffuse.diffuse_src_manager:DiffuseCompChain.main',
        'fermipy-diffuse-analysis = fermipy.diffuse.diffuse_analysis:DiffuseAnalysisChain.main',
        'fermipy-job-archive = fermipy.jobs.job_archive:main_browse',
        'fermipy-file-archive = fermipy.jobs.file_archive:main_browse',
        'fermipy-analyze-roi = fermipy.jobs.target_analysis:AnalyzeROI.main',
        'fermipy-analyze-roi-sg = fermipy.jobs.target_analysis:AnalyzeROI.main',
        'fermipy-analyze-sed = fermipy.jobs.target_analysis:AnalyzeSED.main',
        'fermipy-analyze-sed-sg = fermipy.jobs.target_analysis:AnalyzeSED.main',
        'fermipy-copy-base-roi = fermipy.jobs.target_sim:CopyBaseROI.main',
        'fermipy-copy-base-roi-sg = fermipy.jobs.target_sim:CopyBaseROI_SG.main',
        'fermipy-random-dir-gen = fermipy.jobs.target_sim:RandomDirGen.main',
        'fermipy-random-dir-gen-sg = fermipy.jobs.target_sim:RandomDirGen_SG.main',
        'fermipy-simulate-roi = fermipy.jobs.target_sim:SimulateROI.main',
        'fermipy-simulate-roi-sg = fermipy.jobs.target_sim:SimulateROI_SG.main',
        'fermipy-collect-sed = fermipy.jobs.target_collect:CollectSED.main',
        'fermipy-collect-sed-sg = fermipy.jobs.target_collect:CollectSED_SG.main',
        'fermipy-plot-castro = fermipy.jobs.target_plotting:PlotCastro.main',
        'fermipy-plot-castro-sg = fermipy.jobs.target_plotting:PlotCastro_SG.main',
    ]},
    install_requires=[
        'numpy >= 1.6.1',
        'astropy >= 1.2.1',
        'matplotlib >= 1.5.0',
        'scipy >= 0.14',
        'pyyaml',
        'healpy',
        'gammapy',
    ],
    extras_require=dict(
        all=[],
    ),
)
