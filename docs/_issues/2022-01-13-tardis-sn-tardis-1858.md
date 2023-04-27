---
tags: testing-vertical_traffic_light
title: "Address fixtures that are not being used"
html_url: "https://github.com/tardis-sn/tardis/issues/1858"
user: atharva-2001
repo: tardis-sn/tardis
---

**Describe the bug**
<!-- A clear and concise description of what the bug is -->
According to [pytest dead fixtures](https://github.com/jllorencetti/pytest-deadfixtures ), there are some fixtures which are not being used:
```
Fixture name: refdata, location: tardis/gui/tests/test_gui.py:14
Fixture name: verysimple_collection, location: tardis/montecarlo/montecarlo_numba/tests/conftest.py:28
Fixture name: runner, location: tardis/montecarlo/tests/conftest.py:8
Fixture name: expected_ff_emissivity, location: tardis/montecarlo/tests/test_montecarlo.py:100
Fixture name: ion_edges, location: tardis/montecarlo/tests/test_montecarlo.py:113
Fixture name: continuum_compare_data_fname, location: tardis/montecarlo/tests/test_montecarlo.py:82
Fixture name: continuum_compare_data, location: tardis/montecarlo/tests/test_montecarlo.py:88
Fixture name: data_path, location: tardis/montecarlo/tests/test_packet_source.py:12
```


**To Reproduce**
<!-- Steps to reproduce the behavior, link to a notebook or a copy-pastable example -->
Install pytest dead fixtures and run it on TARDIS

**Screenshots**
<!-- If applicable, add screenshots to help explain your problem -->


**System**
 - OS:
    - [X] GNU/Linux
    - [ ] macOS

 - Environment (`conda list`):
<details>
  <summary>Environment</summary>
  
  ```
 # packages in environment at /home/atharva/.conda/envs/tardis_reinstall:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                 conda_forge    conda-forge
_openmp_mutex             4.5                       1_gnu    conda-forge
alabaster                 0.7.12                     py_0    conda-forge
alsa-lib                  1.2.3                h516909a_0    conda-forge
anyio                     3.4.0                    pypi_0    pypi
argcomplete               1.12.3             pyhd8ed1ab_2    conda-forge
argon2-cffi               21.1.0           py37h5e8e339_2    conda-forge
astropy                   3.2.3            py37h516909a_0    conda-forge
astropy-sphinx-theme      1.1                        py_0    conda-forge
async_generator           1.10                       py_0    conda-forge
atk-1.0                   2.36.0               h3371d22_4    conda-forge
attrs                     21.2.0             pyhd8ed1ab_0    conda-forge
babel                     2.9.1              pyh44b312d_0    conda-forge
backcall                  0.2.0              pyh9f0ad1d_0    conda-forge
backports                 1.0                        py_2    conda-forge
backports.functools_lru_cache 1.6.4              pyhd8ed1ab_0    conda-forge
beautifulsoup4            4.10.0             pyha770c72_0    conda-forge
black                     21.11b0            pyhd8ed1ab_0    conda-forge
bleach                    4.1.0              pyhd8ed1ab_0    conda-forge
blosc                     1.21.0               h9c3ff4c_0    conda-forge
brotli                    1.0.9                h7f98852_6    conda-forge
brotli-bin                1.0.9                h7f98852_6    conda-forge
brotlipy                  0.7.0           py37h5e8e339_1003    conda-forge
bzip2                     1.0.8                h7f98852_4    conda-forge
c-ares                    1.18.1               h7f98852_0    conda-forge
ca-certificates           2021.10.8            ha878542_0    conda-forge
cached-property           1.5.2                hd8ed1ab_1    conda-forge
cached_property           1.5.2              pyha770c72_1    conda-forge
cairo                     1.16.0            h6cf1ce9_1008    conda-forge
certifi                   2021.10.8        py37h89c1867_1    conda-forge
cffi                      1.15.0           py37h036bc23_0    conda-forge
charset-normalizer        2.0.8              pyhd8ed1ab_0    conda-forge
click                     8.0.3            py37h89c1867_1    conda-forge
colorama                  0.4.4              pyh9f0ad1d_0    conda-forge
commonmark                0.9.1                      py_0    conda-forge
coverage                  6.1.2            py37h5e8e339_0    conda-forge
cryptography              36.0.0           py37hf1a17b8_0    conda-forge
cycler                    0.11.0             pyhd8ed1ab_0    conda-forge
dataclasses               0.8                pyhc8e2a94_3    conda-forge
dbus                      1.13.6               h48d8840_2    conda-forge
debugpy                   1.5.1            py37hcd2ae1e_0    conda-forge
decorator                 4.4.2                      py_0    conda-forge
defusedxml                0.7.1              pyhd8ed1ab_0    conda-forge
docutils                  0.16             py37h89c1867_3    conda-forge
dot2tex                   2.11.3                   pypi_0    pypi
entrypoints               0.3             pyhd8ed1ab_1003    conda-forge
expat                     2.4.1                h9c3ff4c_0    conda-forge
font-ttf-dejavu-sans-mono 2.37                 hab24e00_0    conda-forge
font-ttf-inconsolata      3.000                h77eed37_0    conda-forge
font-ttf-source-code-pro  2.038                h77eed37_0    conda-forge
font-ttf-ubuntu           0.83                 hab24e00_0    conda-forge
fontconfig                2.13.1            hba837de_1005    conda-forge
fonts-conda-ecosystem     1                             0    conda-forge
fonts-conda-forge         1                             0    conda-forge
fonttools                 4.28.2           py37h5e8e339_0    conda-forge
freetype                  2.10.4               h0708190_1    conda-forge
fribidi                   1.0.10               h36c2ea0_0    conda-forge
future                    0.18.2           py37h89c1867_4    conda-forge
gdk-pixbuf                2.42.6               h04a7f16_0    conda-forge
geos                      3.10.1               h9c3ff4c_1    conda-forge
gettext                   0.19.8.1          h73d1719_1008    conda-forge
giflib                    5.2.1                h36c2ea0_2    conda-forge
git-lfs                   3.0.2                ha770c72_0    conda-forge
glib                      2.70.1               h780b84a_0    conda-forge
glib-tools                2.70.1               h780b84a_0    conda-forge
graphite2                 1.3.13            h58526e2_1001    conda-forge
graphviz                  2.49.3               h85b4f2f_0    conda-forge
gst-plugins-base          1.18.5               hf529b03_2    conda-forge
gstreamer                 1.18.5               h9f60fe5_2    conda-forge
gtk2                      2.24.33              h539f30e_1    conda-forge
gts                       0.7.6                h64030ff_2    conda-forge
h5py                      3.3.0           nompi_py37ha3df211_100    conda-forge
harfbuzz                  3.1.1                h83ec7ef_0    conda-forge
hdf5                      1.10.6          nompi_h7c3c948_1111    conda-forge
hypothesis                6.27.2             pyhd8ed1ab_0    conda-forge
icu                       68.2                 h9c3ff4c_0    conda-forge
idna                      3.1                pyhd3deb0d_0    conda-forge
imagesize                 1.3.0              pyhd8ed1ab_0    conda-forge
importlib-metadata        4.8.2            py37h89c1867_0    conda-forge
importlib_metadata        4.8.2                hd8ed1ab_0    conda-forge
iniconfig                 1.1.1              pyh9f0ad1d_0    conda-forge
ipykernel                 6.5.0            py37h6531663_1    conda-forge
ipytest                   0.11.0                   pypi_0    pypi
ipython                   7.30.0           py37h89c1867_0    conda-forge
ipython_genutils          0.2.0                      py_1    conda-forge
ipywidgets                7.6.5              pyhd8ed1ab_0    conda-forge
jbig                      2.1               h7f98852_2003    conda-forge
jedi                      0.18.1           py37h89c1867_0    conda-forge
jinja2                    3.0.3              pyhd8ed1ab_0    conda-forge
jpeg                      9d                   h36c2ea0_0    conda-forge
json5                     0.9.6                    pypi_0    pypi
jsonpointer               2.0                        py_0    conda-forge
jsonschema                3.2.0              pyhd8ed1ab_3    conda-forge
jupyter                   1.0.0            py37h89c1867_7    conda-forge
jupyter-contrib-core      0.3.3                    pypi_0    pypi
jupyter-contrib-nbextensions 0.5.1                    pypi_0    pypi
jupyter-highlight-selected-word 0.2.0                    pypi_0    pypi
jupyter-latex-envs        1.4.6                    pypi_0    pypi
jupyter-nbextensions-configurator 0.4.1                    pypi_0    pypi
jupyter-server            1.13.1                   pypi_0    pypi
jupyter_client            7.1.0              pyhd8ed1ab_0    conda-forge
jupyter_console           6.4.0              pyhd8ed1ab_0    conda-forge
jupyter_core              4.9.1            py37h89c1867_1    conda-forge
jupyterlab                3.2.6                    pypi_0    pypi
jupyterlab-server         2.10.3                   pypi_0    pypi
jupyterlab_pygments       0.1.2              pyh9f0ad1d_0    conda-forge
jupyterlab_widgets        1.0.2              pyhd8ed1ab_0    conda-forge
kiwisolver                1.3.2            py37h2527ec5_1    conda-forge
krb5                      1.19.2               hcc1bbae_3    conda-forge
lab                       7.0                      pypi_0    pypi
latexcodec                2.0.1              pyh9f0ad1d_0    conda-forge
lcms2                     2.12                 hddcbb42_0    conda-forge
ld_impl_linux-64          2.36.1               hea4e1c9_2    conda-forge
lerc                      3.0                  h9c3ff4c_0    conda-forge
libblas                   3.9.0                8_openblas    conda-forge
libbrotlicommon           1.0.9                h7f98852_6    conda-forge
libbrotlidec              1.0.9                h7f98852_6    conda-forge
libbrotlienc              1.0.9                h7f98852_6    conda-forge
libcblas                  3.9.0                8_openblas    conda-forge
libclang                  11.1.0          default_ha53f305_1    conda-forge
libcurl                   7.80.0               h2574ce0_0    conda-forge
libdeflate                1.8                  h7f98852_0    conda-forge
libedit                   3.1.20191231         he28a2e2_2    conda-forge
libev                     4.33                 h516909a_1    conda-forge
libevent                  2.1.10               h9b69904_4    conda-forge
libffi                    3.4.2                h7f98852_5    conda-forge
libgcc-ng                 11.2.0              h1d223b6_11    conda-forge
libgd                     2.3.3                h6ad9fb6_0    conda-forge
libgfortran-ng            7.5.0               h14aa051_19    conda-forge
libgfortran4              7.5.0               h14aa051_19    conda-forge
libglib                   2.70.1               h174f98d_0    conda-forge
libgomp                   11.2.0              h1d223b6_11    conda-forge
libiconv                  1.16                 h516909a_0    conda-forge
liblapack                 3.9.0                8_openblas    conda-forge
libllvm10                 10.0.1               he513fc3_3    conda-forge
libllvm11                 11.1.0               hf817b99_2    conda-forge
libnghttp2                1.43.0               h812cca2_1    conda-forge
libnsl                    2.0.0                h7f98852_0    conda-forge
libogg                    1.3.4                h7f98852_1    conda-forge
libopenblas               0.3.12          pthreads_hb3c22a3_1    conda-forge
libopus                   1.3.1                h7f98852_1    conda-forge
libpng                    1.6.37               h21135ba_2    conda-forge
libpq                     13.5                 hd57d9b9_0    conda-forge
librsvg                   2.52.4               hc3c00ef_0    conda-forge
libsodium                 1.0.18               h36c2ea0_1    conda-forge
libssh2                   1.10.0               ha56f1ee_2    conda-forge
libstdcxx-ng              11.2.0              he4da1e4_11    conda-forge
libtiff                   4.3.0                h6f004c6_2    conda-forge
libtool                   2.4.6             h9c3ff4c_1008    conda-forge
libuuid                   2.32.1            h7f98852_1000    conda-forge
libvorbis                 1.3.7                h9c3ff4c_0    conda-forge
libwebp                   1.2.1                h3452ae3_0    conda-forge
libwebp-base              1.2.1                h7f98852_0    conda-forge
libxcb                    1.13              h7f98852_1004    conda-forge
libxkbcommon              1.0.3                he3ba5ed_0    conda-forge
libxml2                   2.9.12               h72842e0_0    conda-forge
libxslt                   1.1.33               h15afd5d_2    conda-forge
libzlib                   1.2.11            h36c2ea0_1013    conda-forge
llvmlite                  0.36.0           py37h9d7f4d0_0    conda-forge
lxml                      4.6.4            py37h77fd288_0    conda-forge
lz4-c                     1.9.3                h9c3ff4c_1    conda-forge
lzo                       2.10              h516909a_1000    conda-forge
markupsafe                2.0.1            py37h5e8e339_1    conda-forge
matplotlib                3.5.0            py37h89c1867_0    conda-forge
matplotlib-base           3.5.0            py37h1058ff1_0    conda-forge
matplotlib-inline         0.1.3              pyhd8ed1ab_0    conda-forge
mistune                   0.8.4           py37h5e8e339_1005    conda-forge
mock                      4.0.3            py37h89c1867_2    conda-forge
more-itertools            8.12.0             pyhd8ed1ab_0    conda-forge
munkres                   1.1.4              pyh9f0ad1d_0    conda-forge
mypy_extensions           0.4.3            py37h89c1867_4    conda-forge
mysql-common              8.0.27               ha770c72_1    conda-forge
mysql-libs                8.0.27               hfa10184_1    conda-forge
nbclassic                 0.3.4                    pypi_0    pypi
nbclient                  0.5.9              pyhd8ed1ab_0    conda-forge
nbconvert                 6.3.0            py37h89c1867_1    conda-forge
nbformat                  5.1.3              pyhd8ed1ab_0    conda-forge
nbsphinx                  0.8.7              pyhd8ed1ab_0    conda-forge
ncurses                   6.2                  h58526e2_4    conda-forge
nest-asyncio              1.5.1              pyhd8ed1ab_0    conda-forge
networkx                  2.5.1              pyhd8ed1ab_0    conda-forge
nomkl                     1.0                  h5ca1d4c_0    conda-forge
notebook                  6.4.6              pyha770c72_0    conda-forge
nspr                      4.32                 h9c3ff4c_1    conda-forge
nss                       3.72                 hb5efdd6_0    conda-forge
numba                     0.53.1           py37hb11d6e1_1    conda-forge
numexpr                   2.7.3           py37hfe5f03c_102    conda-forge
numpy                     1.19.5           py37h038b26d_2    conda-forge
numpydoc                  1.1.0                      py_1    conda-forge
olefile                   0.46               pyh9f0ad1d_1    conda-forge
openjpeg                  2.4.0                hb52868f_1    conda-forge
openmc                    0.12.2           py37hcab8d4c_1    conda-forge
openssl                   1.1.1l               h7f98852_0    conda-forge
packaging                 21.3               pyhd8ed1ab_0    conda-forge
pandas                    1.0.5            py37h0da4684_0    conda-forge
pandoc                    2.16.2               h7f98852_0    conda-forge
pandocfilters             1.5.0              pyhd8ed1ab_0    conda-forge
pango                     1.48.10              h54213e6_2    conda-forge
parso                     0.8.2              pyhd8ed1ab_0    conda-forge
pathspec                  0.9.0              pyhd8ed1ab_0    conda-forge
pbr                       5.8.0              pyhd8ed1ab_0    conda-forge
pcre                      8.45                 h9c3ff4c_0    conda-forge
pexpect                   4.8.0              pyh9f0ad1d_2    conda-forge
pickle5                   0.0.12           py37h5e8e339_0    conda-forge
pickleshare               0.7.5                   py_1003    conda-forge
pillow                    8.4.0            py37h0f21c89_0    conda-forge
pip                       21.3.1             pyhd8ed1ab_0    conda-forge
pixman                    0.40.0               h36c2ea0_0    conda-forge
platformdirs              2.3.0              pyhd8ed1ab_0    conda-forge
plotly                    5.4.0              pyhd8ed1ab_0    conda-forge
pluggy                    1.0.0            py37h89c1867_2    conda-forge
prometheus_client         0.12.0             pyhd8ed1ab_0    conda-forge
prompt-toolkit            3.0.22             pyha770c72_0    conda-forge
prompt_toolkit            3.0.22               hd8ed1ab_0    conda-forge
psutil                    5.8.0            py37h5e8e339_2    conda-forge
pthread-stubs             0.4               h36c2ea0_1001    conda-forge
ptyprocess                0.7.0              pyhd3deb0d_0    conda-forge
py                        1.11.0             pyh6c4a22f_0    conda-forge
pybtex                    0.24.0           py37h89c1867_1    conda-forge
pybtex-docutils           1.0.1            py37h89c1867_1    conda-forge
pycparser                 2.21               pyhd8ed1ab_0    conda-forge
pydocstyle                6.1.1              pyhd3eb1b0_0  
pygments                  2.10.0             pyhd8ed1ab_0    conda-forge
pygraphviz                1.7              py37ha333112_1    conda-forge
pyne                      0.7.0           nomoab_openmc_py37h8d68778_1    conda-forge
pyopenssl                 21.0.0             pyhd8ed1ab_0    conda-forge
pyparsing                 3.0.6              pyhd8ed1ab_0    conda-forge
pyqt                      5.12.3           py37h89c1867_8    conda-forge
pyqt-impl                 5.12.3           py37hac37412_8    conda-forge
pyqt5-sip                 4.19.18          py37hcd2ae1e_8    conda-forge
pyqtchart                 5.12             py37he336c9b_8    conda-forge
pyqtwebengine             5.12.1           py37he336c9b_8    conda-forge
pyrsistent                0.18.0           py37h5e8e339_0    conda-forge
pysocks                   1.7.1            py37h89c1867_4    conda-forge
pytables                  3.6.1            py37h0c4f3e0_3    conda-forge
pytest                    6.2.5            py37h89c1867_1    conda-forge
pytest-arraydiff          0.3                        py_0    conda-forge
pytest-astropy            0.9.0              pyhd8ed1ab_0    conda-forge
pytest-astropy-header     0.1.2                      py_0    conda-forge
pytest-cov                3.0.0              pyhd8ed1ab_0    conda-forge
pytest-deadfixtures       2.2.1                    pypi_0    pypi
pytest-doctestplus        0.11.1             pyhd8ed1ab_0    conda-forge
pytest-filter-subpackage  0.1.1                      py_0    conda-forge
pytest-html               3.1.1              pyhd8ed1ab_0    conda-forge
pytest-leaks              0.3.1                    pypi_0    pypi
pytest-metadata           1.11.0             pyhd3deb0d_0    conda-forge
pytest-mock               3.6.1              pyhd8ed1ab_0    conda-forge
pytest-openfiles          0.5.0                      py_0    conda-forge
pytest-remotedata         0.3.2              pyh9f0ad1d_0    conda-forge
python                    3.7.12          hb7a2778_100_cpython    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python-dokuwiki           1.3.1              pyhd8ed1ab_0    conda-forge
python_abi                3.7                     2_cp37m    conda-forge
pytz                      2021.3             pyhd8ed1ab_0    conda-forge
pyyaml                    6.0              py37h5e8e339_3    conda-forge
pyzmq                     22.3.0           py37h336d617_1    conda-forge
qgrid                     1.3.1              pyhd8ed1ab_3    conda-forge
qt                        5.12.9               hda022c4_4    conda-forge
qtconsole                 5.2.1              pyhd8ed1ab_0    conda-forge
qtpy                      1.11.2             pyhd8ed1ab_0    conda-forge
readline                  8.1                  h46c0cb4_0    conda-forge
recommonmark              0.7.1              pyhd8ed1ab_0    conda-forge
regex                     2021.11.10       py37h5e8e339_0    conda-forge
requests                  2.26.0             pyhd8ed1ab_1    conda-forge
scipy                     1.5.3            py37h8911b10_0    conda-forge
send2trash                1.8.0              pyhd8ed1ab_0    conda-forge
setuptools                59.2.0           py37h89c1867_0    conda-forge
setuptools-scm            6.3.2              pyhd8ed1ab_0    conda-forge
setuptools_scm            6.3.2                hd8ed1ab_0    conda-forge
shapely                   1.8.0            py37h9b0f7a3_4    conda-forge
simplejson                3.17.6                   pypi_0    pypi
six                       1.16.0             pyh6c4a22f_0    conda-forge
snakeviz                  2.1.1              pyhd8ed1ab_0    conda-forge
sniffio                   1.2.0                    pypi_0    pypi
snowballstemmer           2.2.0              pyhd8ed1ab_0    conda-forge
sortedcontainers          2.4.0              pyhd8ed1ab_0    conda-forge
soupsieve                 2.3                pyhd8ed1ab_0    conda-forge
sphinx                    4.3.0              pyh6c4a22f_0    conda-forge
sphinx-astropy            1.6.0              pyhd8ed1ab_0    conda-forge
sphinx-automodapi         0.13                       py_0    conda-forge
sphinx-gallery            0.10.1             pyhd8ed1ab_0    conda-forge
sphinx-jsonschema         1.17.1             pyhd8ed1ab_0    conda-forge
sphinx_bootstrap_theme    0.8.0                      py_0    conda-forge
sphinx_rtd_theme          1.0.0              pyhd8ed1ab_0    conda-forge
sphinxcontrib-apidoc      0.3.0                      py_1    conda-forge
sphinxcontrib-applehelp   1.0.2                      py_0    conda-forge
sphinxcontrib-bibtex      2.4.1              pyhd8ed1ab_0    conda-forge
sphinxcontrib-devhelp     1.0.2                      py_0    conda-forge
sphinxcontrib-htmlhelp    2.0.0              pyhd8ed1ab_0    conda-forge
sphinxcontrib-jsmath      1.0.1                      py_0    conda-forge
sphinxcontrib-qthelp      1.0.3                      py_0    conda-forge
sphinxcontrib-serializinghtml 1.1.5              pyhd8ed1ab_1    conda-forge
sqlite                    3.36.0               h9cd32fc_2    conda-forge
tenacity                  8.0.1              pyhd8ed1ab_0    conda-forge
terminado                 0.12.1           py37h89c1867_1    conda-forge
testpath                  0.5.0              pyhd8ed1ab_0    conda-forge
tk                        8.6.11               h27826a3_1    conda-forge
toml                      0.10.2             pyhd8ed1ab_0    conda-forge
tomli                     1.2.2              pyhd8ed1ab_0    conda-forge
tornado                   6.1              py37h5e8e339_2    conda-forge
tqdm                      4.62.3             pyhd8ed1ab_0    conda-forge
traitlets                 5.1.1              pyhd8ed1ab_0    conda-forge
txt2tags                  3.7                      pypi_0    pypi
typed-ast                 1.5.0            py37h5e8e339_0    conda-forge
typing_extensions         4.0.0              pyha770c72_0    conda-forge
uncertainties             3.1.6              pyhd8ed1ab_0    conda-forge
unicodedata2              13.0.0.post2     py37h5e8e339_4    conda-forge
urllib3                   1.26.7             pyhd8ed1ab_0    conda-forge
wcwidth                   0.2.5              pyh9f0ad1d_2    conda-forge
webencodings              0.5.1                      py_1    conda-forge
websocket-client          1.2.3                    pypi_0    pypi
wheel                     0.37.0             pyhd8ed1ab_1    conda-forge
widgetsnbextension        3.5.2            py37h89c1867_1    conda-forge
xorg-kbproto              1.0.7             h7f98852_1002    conda-forge
xorg-libice               1.0.10               h7f98852_0    conda-forge
xorg-libsm                1.2.3             hd9c2040_1000    conda-forge
xorg-libx11               1.7.2                h7f98852_0    conda-forge
xorg-libxau               1.0.9                h7f98852_0    conda-forge
xorg-libxdmcp             1.1.3                h7f98852_0    conda-forge
xorg-libxext              1.3.4                h7f98852_1    conda-forge
xorg-libxrender           0.9.10            h7f98852_1003    conda-forge
xorg-renderproto          0.11.1            h7f98852_1002    conda-forge
xorg-xextproto            7.3.0             h7f98852_1002    conda-forge
xorg-xproto               7.0.31            h7f98852_1007    conda-forge
xz                        5.2.5                h516909a_1    conda-forge
yaml                      0.2.5                h516909a_0    conda-forge
zeromq                    4.3.4                h9c3ff4c_1    conda-forge
zipp                      3.6.0              pyhd8ed1ab_0    conda-forge
zlib                      1.2.11            h36c2ea0_1013    conda-forge
zstd                      1.5.0                ha95c52a_0    conda-forge

  ```
</details>

**Additional context**
<!-- Add any other context about the problem here -->
