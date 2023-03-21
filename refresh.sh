python3 update_version_clean_nb.py

vers_full=`cat scselpy/version.py` #rewrite this
vers_cut=`echo $vers_full | cut -d "\"" -f2-`
vers=${vers_cut%?}
echo $vers
jupyter nbconvert --to Markdown docs/source/Tutorial.ipynb
mv docs/source/Tutorial.ipynb Tutorial.ipynb
jupyter nbconvert --to Markdown docs/source/Mock.ipynb
rm docs/source/Mock.ipynb


echo -e '# Tutorial\n```{eval-rst}\n.. role:: small\n```\n\n```{eval-rst}\n.. role:: smaller\n```' |cat - docs/source/Tutorial.md > /tmp/out && mv /tmp/out docs/source/Tutorial.md
echo -e '# Mock\n```{eval-rst}\n.. role:: small\n```\n\n```{eval-rst}\n.. role:: smaller\n```' |cat - docs/source/Mock.md > /tmp/out && mv /tmp/out docs/source/Mock.md

python3 -m build
python3 -m pip install dist/scselpy-$vers-py3-none-any.whl


