.. -*- mode: rst -*-

|GitHubActionsBadge|_ |ReadTheDocsBadge|_

.. |GitHubActionsBadge| image:: https://github.com/simai-ml/how-to-opensource/actions/workflows/python-package-conda.yml/badge.svg
.. _GitHubActionsBadge: https://github.com/simai-ml/how-to-opensource/actions

.. |ReadTheDocsBadge| image:: https://readthedocs.org/projects/how-to-opensource/badge
.. _ReadTheDocsBadge: https://how-to-opensource.readthedocs.io/en/latest

BBL - Publier un package en open-source en dix étapes clés
==========================================================

Quelles sont les étapes indispensables pour publier un package Python en open-source ? Depuis l’écriture d’un code propre et la rédaction de la documentation, jusqu’aux tests d’intégration continue et au processus de packaging, nous passerons en revue les dix points clés pour une publication d’un package Python en open-source. Pour ce faire, nous prendrons l’exemple d’un toy model que nous publierons sur github et pypi en moins de deux heures.

Pré-requis
==========

1. Avoir un compte GitHub
2. Faire un **Fork** du dépôt (bouton en haut à droite de GitHub)
3. Avoir une installation locale de conda

Si vous n'avez pas de conda installé : téléchargez l'installeur Conda_ ou exécutez les commandes suivantes:

.. code:: shell-session

  $ wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-MacOSX-x86_64.sh -O miniconda.sh
  $ chmod +x miniconda.sh
  $ bash miniconda.sh

Attention à bien accepter la demande d'initialisation.

Exercice n°1: Mise en place de l'environnement
==============================================

Clonez votre dépôt forké:

.. code:: shell-session

  $ git clone https://github.com/COMPTE/how-to-opensource.git

Installez et activez l'EnvConda_:

.. code:: shell-session

  cd how-to-opensource
  conda env create -f environment.dev.yml
  conda activate how_to_opensource

Créer une branche de travail et supprimez la correction :

.. code:: shell-session

  git checkout -b work
  ./start.sh

Vous pouvez commencer !

Exercice n°2: Création d'un module et d'une fonction
====================================================

Nous allons maintenant créer dans le Module_ **how_to_opensource** une nouvelle fonction calculant la somme de deux vecteurs.
Pour cela rendez vous dans le fichier **how_to_opensource/core.py** et créez une nouvelle fonction `add_two_vectors`. Il est maintenant possible de tester interactivement la méthode :

.. code:: python

  import numpy as np
  from how_to_opensource import add_two_vectors
  add_two_vectors(np.ones(2), np.ones(2))

Exercice n°3: Création d'un test unitaire
=========================================

Il convient maintenant de tester cette fonction avec PyTest_. Une méthode standard pour élargir rapidement le domaine testé est d'utiliser Parameterize_ pour paramétriser les fonctions de test.
Dans **how_to_opensource/tests/test_core.py** ajoutez une fonction de test validant le bon fonctionnement de `add_two_vectors` en testant différentes dimensions de vecteurs. Lancez maintenant le test en générant les métriques validants que vos tests couvrent bien le code:

.. code:: shell-session

  $ pytest -vs --cov-branch --cov=how_to_opensource --pyargs how_to_opensource

Exercice n°4: Documentation de la fonction
==========================================

Numpydoc_ propose une méthode de documentation efficace. Ajoutez une documentation à `add_two_vectors` spécifiant ses paramètres, sa sortie et en y incluant une DocTest_. Lancez ensuite la procédure de test en incluant cette fois le test de la documentation.

.. code:: shell-session

  $ pytest -vs --doctest-modules --cov-branch --cov=how_to_opensource --pyargs how_to_opensource

Exercice n°5: Typing
====================

Une pratique courante pour rendre plus robuste un package consiste à utiliser le typing pour tout ou partie du code. Si l'interpréteur python ne vérifie pas ces types à l'exécution, le langage python propose néanmoins le vocabulaire et la grammaire nécessaire à la définition de ces types par l'intermédiaire du module Typing_.
Typez maintenant les définitions de `add_two_vectors` et de sa fonction de test. Il est aussi possible d'ajouter un test à l'exécution pour valider que les entrées se conforment au type attendu. Enfin lancez l'analyseur statique de code le second statique utilisant MyPy_.

.. code:: shell-session

  $ mypy how_to_opensource --strict

Exercice n°6: Intégration continue du code
==========================================

Afin d'assurer un niveau de qualité constant, particulièrement dans le cas d'un projet opensource avec de multiples contributeurs, il est indispensable d'automatiser le processus d'intégration des changements réalisés. C'est à ce point que répond l'intégration continue. Se basant sur la description d'un pipeline incluant build, test et déploiement, les outils d'integration continue, par exemple GitHubActions_ ou TravisCI_ en permettent l'automatisation. Cela apporte les valeurs suivantes:

- minimiser la charge de travail pour les concepteurs
- supprimer les erreurs arrivent dans toute action "à la main"
- réduire le temps nécessaire à la détection et l'analyse de problèmes car chaque changement est validé granulairement
- réduire le temps de cycle pour la livraison de nouvelles fonctionnalités tout en en améliorant la qualité

Nous allons utiliser les GitHub actions, pour cela sur la GiHub de votre projet rendez vous sur l'onglet **Actions**. Pour scréer notre workflow d'intégration continue nous allons partir du template **Python Package using Anaconda**, cliquez sur **Setup this workflow**. Modifiez ensuite les étapes du workflow pour coller aux éléments défins précédement:

- déploiement sur Python 3.9 uniquement
- installation par environment.yml
- pas d'analyse statique de code (suppression de la section Lint)
- complétion de la commande de test

Une fois le fichier créé ajouté au dépôt, vous pouvez suivre l'execution du pipeline depuis l'interface de GitHub. Un mail vous sera automatiquement envoyé en fin d'execution pour vous informer des résultats.

Exercice n°7: Génération de la documentation
============================================

Avoir une documentation à jour est indispensable autant pour les utilisateurs que pour les contributeurs. Afin de faciliter la création et la maintenance de celle-ci nous allons utiliser Sphinx_. Le quick start de Sphinx permet l'initialisation rapide des éléments nécessaires.

.. code:: shell-session

  $ sphinx-quickstart doc

Note: il n'est pas nécessaire de séparer les répertoires sources et build dans notre cas simple.
Pour génerer la documentation il vous suffit maintenant d'executer le script nouvellement créé:

.. code:: shell-session

  $ cd doc
  $ make html
  $ cd -

La documentation a été générée dans le repertoire **doc/_build**, vous pouvez la consulter dans votre navigateur web, elle est belle, mais vide. En plus de la rédaction que vous ne manquerez pas d'ajouter, il est important de capitaliser sur la documentation écrite à l'exercice n°4. Pour ce faire, il faut d'abord modifier le fichier **doc/conf.py** pour ajouter `'sphinx.ext.autodoc'`, `'sphinx.ext.napoleon'`, `'sphinx.ext.autodoc'` et `'sphinx_autodoc_typehints'` à la liste des extensions et enfin d'ajouter la demande d'extraction de documentation du module dans **doc/index.rst** qui sera par ailleurs le point d'entrée de toute rédactions additionnelle.

.. code::

  .. automodule:: how_to_opensource
     :members:

Afin de permettre de trouver le module et d'activer la prise en compte des types, ajoutez les lignes suivantes au fichier **doc/conf.py**:

.. code:: python

  import sys
  sys.path.append('../')
  napoleon_use_param = True

Une méthode efficace pour enrichir la documentation consiste à ajouter des exemples que l'on met en valeur à l'aide de SphinxGallery_.
Dans **doc/conf.py**, ajoutez l'extension `'sphinx_gallery.gen_gallery'`, puis définisez la configuration de la gallerie:

.. code:: python

  sphinx_gallery_conf = {
    'examples_dirs': '../examples',   # path to your example scripts
    'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
  }

Enfin il est nécessaire d'inclure cette galerie à la racine de la documentation, dans **doc/index.rst** ajoutez son inclusion:

.. code::

  .. toctree::
    :maxdepth: 2

    auto_examples/index

Exercice n°8: Intégration continue de la documentation
======================================================

Pour diffuser cette documentation il est nécessaire de la publier sur un site publique, par exemple en utilisant ReadTheDocs_. Ce dernier réalisera les tâches définies dans le fichier **.readthedocs.yml**, ajoutez donc ce fichier au dépôt avec le contenu suivant:

.. code::
  version: 2

  build:
    image: latest

  conda:
    environment: environment.yml
    
  sphinx:
    builder: html
    configuration: doc/conf.py
    fail_on_warning: false

Ensuite, créez un compte gratuit sur ReadTheDocs_ en utilisant votre login GitHUB. Une fois inscrit et connecté, importez votre projet GitHUB, après avoir soigneusement choisi la branche et la version, lancez la compilation. Suivez son bon déroulement et vérifiez que la documentation produite est conforme à vos attentes.

Nous avons maintenant en place un pipeline automatique de publication de documentation. Nous allons maintenant ajouter l'intégration continue de cette documentation et pour cela utiliser le service CircleIO_

Exercice n°9: Packaging
=======================

De façon à offrir une API claire à l'ensemble des modules de notre projet (certes il n'y en a qu'un en l'état mais cela est voué à changer), il est utile de créer un package_ qui permet d'avoir un espace de nommage encapuslant les modules et variables. Pour cela, il est nécessaire d'ajouter un fichier **setup.py** à notre projet, et de le définir, vous pouvez pour cela partir de ce tutoriel_. Il ne vous reste plus qu'à builder votre package

.. code:: shell-session

  $ python setup.py build

TODO ajouter les dependences (incl. extradeps)

Exercice n°10: Gestion du dépôt
===============================

Notre package est maintenant en place, prêt à être publié et ouvert à sa communauté d'utilisateurs et de contributeurs. Il maintenant nécessaire de donner à ses deux populations les outils dont ils ont besoin.
Une accessibilité simple et maitrisée pour les premiers, de clarté sur les règles de leur engagement pour les seconds.

Pour faciliter l'accessibilité du package, sa mise à disposition sur PiPy est un *defacto* standard. Nous allons donc ajouter à nos workflow d'intégration continue cette publication. Elle sera déclenchée par la release d'une version du package, permettant un contrôle explicite des niveaux de code qualifiés et partagés. Ce versioning permet aussi aux consommateurs de maitriser l'inclusion du package dans leur projet en en contrôlant par exemple les versions utilisées.
Dans la mesure où ce nom de version va se retrouver à plusieurs endroits (setup.py, doc/conf.py, ...), et pour ne pas risquer d'erreurs dans le maintien en cohérence de cette information à plusieurs endroits, il est possible d'utiliser bump2version_. Pour cela créez un fichier **.bumpversion.cfg** à la racine du projet, ce dernier va définir dans quel fichier remplacer automatiquement le numéro de version. Ajoutez y le contenu ci-dessous et assurez vous que tous les fichiers contiennent initalement les mêmes numéros de version, par la suite ils seront mis à jour automatiquement :

.. code::

  [bumpversion]
  current_version = 0.0.1
  commit = True
  tag = True

  [bumpversion:file:setup.py]
  search = VERSION = "{current_version}"
  replace = VERSION = "{new_version}"

  [bumpversion:file:how_to_opensource/_version.py]
  search = __version__ = "{current_version}"
  replace = __version__ = "{new_version}"

  [bumpversion:file:doc/conf.py]
  search = version = "{current_version}"
  replace = version = "{new_version}"

Maintenant nous allons mettre en place la publication automatique sur PyPi, pour cela rendez vous dans l'onglet action du projet GitHub. Commençez par créer un compte sur PyPi_. Ajoutez ensuite un nouveau worflow en vous basant sur le template "Publish Python Package".

Enfin il convient d'ajouter de documenter les régles de contribution et d'usage du package. Pour cela rendez vous dans la page **Insights/Community** de GitHub. Cette dernière fournit un moyen simple d'initier les documents nécessaires. Une attention particulière étant bien sûr à porter sur la license, le canon du moment étant BSD3 pour les projets opensource.

TODO ajouter template d'issue
TODO ajouter une pull request

.. _Conda: https://docs.conda.io/en/latest/miniconda.html
.. _EnvConda: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
.. _Module: https://docs.python.org/3/tutorial/modules.html
.. _PyTest: https://docs.pytest.org/en/6.2.x/
.. _Parameterize: https://docs.pytest.org/en/6.2.x/parametrize.html
.. _Numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html
.. _DocTest: https://docs.python.org/3/library/doctest.html
.. _Typing: https://docs.python.org/3/library/typing.html
.. _TravisCI: https://travis-ci.com/
.. _MyPy: http://mypy-lang.org/
.. _Sphinx: https://www.sphinx-doc.org/en/master/index.html
.. _ReadTheDocs: https://readthedocs.org/
.. _SphinxGallery: https://sphinx-gallery.github.io/stable/getting_started.html
.. _CircleIO: https://circleci.com/
.. _GitHubActions: https://github.com/features/actions
.. _package: https://docs.python.org/3/tutorial/modules.html#packages
.. _tutoriel: https://pythonhosted.org/an_example_pypi_project/setuptools.html
.. _bump2version: https://github.com/c4urself/bump2version
.. _PyPi: https://pypi.org/account/register/