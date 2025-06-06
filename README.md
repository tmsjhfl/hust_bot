# Isaac lab for hust robot 

## Installation
- Install Isaac Sim and Isaac Lab by following the [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html)  
    Note that using the conda installation will simplify calling python scripts from the terminal  
      
- Create your own conda env  
    ```bash
    conda create -n lab_bot python=3.10  
    conda activate lab_bot  
      
- Using a python interpreter, install the library in editable mode using:  
    ```bash  
    cd hust_bot/hust_bot  
    python -m pip install -e source/hust_bot  
    ```  
  
- Listing the avaiable tasks in this project  
    ```bash  
    python scripts/list_envs.py  
    # output  
    +--------+---------------------+----------------------------------------------+----------------------------------------------------------+  
    | S. No. | Task Name           | Entry Point                                  |  Config                                                  |                  
    +--------+---------------------+----------------------------------------------+----------------------------------------------------------+  
    |   1    | hustbot-G1-Walk-v0  | hust_bot.tasks.amp.g1_amp.g1_amp_env:G1AmpEnv| hust_bot.tasks.amp.g1_amp.g1_amp_env_cfg:G1AmpWalkEnvCfg |
    +--------+---------------------+----------------------------------------------+----------------------------------------------------------+  
    ```  
- Running a task  
    ```bash  
    python scripts/skrl/train.py --task hustbot-G1-Walk-v0 --num_envs 4096  
    # args: --device cuda:x, --headless and so on
    ```  
- Play a task
    ```bash  
    python scripts/skrl/play.py --task hustbot-G1-Walk-v0 --num_envs 3  
    ```  
## Motion Retarget

- Coming soon

### Set up IDE (Optional)

To setup the IDE, please follow these instructions:

- Run VSCode Tasks, by pressing `Ctrl+Shift+P`, selecting `Tasks: Run Task` and running the `setup_python_env` in the drop down menu.
  When running this task, you will be prompted to add the absolute path to your Isaac Sim installation.

If everything executes correctly, it should create a file .python.env in the `.vscode` directory.
The file contains the python paths to all the extensions provided by Isaac Sim and Omniverse.
This helps in indexing all the python modules for intelligent suggestions while writing code.

### Setup as Omniverse Extension (Optional)

We provide an example UI extension that will load upon enabling your extension defined in `source/hust_bot/hust_bot/ui_extension_example.py`.

To enable your extension, follow these steps:

1. **Add the search path of this project/repository** to the extension manager:
    - Navigate to the extension manager using `Window` -> `Extensions`.
    - Click on the **Hamburger Icon**, then go to `Settings`.
    - In the `Extension Search Paths`, enter the absolute path to the `source` directory of this project/repository.
    - If not already present, in the `Extension Search Paths`, enter the path that leads to Isaac Lab's extension directory directory (`IsaacLab/source`)
    - Click on the **Hamburger Icon**, then click `Refresh`.

2. **Search and enable your extension**:
    - Find your extension under the `Third Party` category.
    - Toggle it to enable your extension.

## Code formatting

We have a pre-commit template to automatically format your code.
To install pre-commit:

```bash
pip install pre-commit
```

Then you can run pre-commit with:

```bash
pre-commit run --all-files
```

## Troubleshooting

### Pylance Missing Indexing of Extensions

In some VsCode versions, the indexing of part of the extensions is missing.
In this case, add the path to your extension in `.vscode/settings.json` under the key `"python.analysis.extraPaths"`.

```json
{
    "python.analysis.extraPaths": [
        "<path-to-ext-repo>/source/hust_bot"
    ]
}
```

### Pylance Crash

If you encounter a crash in `pylance`, it is probable that too many files are indexed and you run out of memory.
A possible solution is to exclude some of omniverse packages that are not used in your project.
To do so, modify `.vscode/settings.json` and comment out packages under the key `"python.analysis.extraPaths"`
Some examples of packages that can likely be excluded are:

```json
"<path-to-isaac-sim>/extscache/omni.anim.*"         // Animation packages
"<path-to-isaac-sim>/extscache/omni.kit.*"          // Kit UI tools
"<path-to-isaac-sim>/extscache/omni.graph.*"        // Graph UI tools
"<path-to-isaac-sim>/extscache/omni.services.*"     // Services tools
...
```