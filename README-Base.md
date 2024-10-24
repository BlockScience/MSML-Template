# MSML Template

The following repository is a template for use in constructing MSML specs. The components in it are marked with DUMMY as they are meant to be replaced but can help in understanding the format of the different pieces.

## The Dummy Model

## SRC Folder
- All the components in here with the exception of implementations are JSON style components that get read into the MSML library for building the specification
    - The MSML documentation details what each type of component is
- Implementations is the folder where Python code can be created to be bound to components
    - For boundary actions, control actions, and policies, the implementations need to have the same name as the different boundary/control/policy options
    - For mechanisms the implementation name should be the same as the mechanism name
    - All will take in state, parameters, and spaces (as a list) and can optionally return spaces (as a list)

## Notebooks Folder

There are four notebooks built in which will listed sequentially by what order in which one would be using them based on project timeline

1. Build Obsidian: The notebook for building the Obsidian reports
- The first code block is for loading the spec, it will flag if certain things are broken or not properly connected
- The second code block writes out the Obsidian vault folder as well as the spec tree
- All that is required is the src folder, implementations and the simulation is not needed for this to run
2. Implementation Playground: The notebook for playing with individual blocks
- The first block of code loads functionality and will flag any components which do not have an implementation loaded in
- For this the full src folder including implementations is required (although partial implementations are ok, it will flag which wirings and components can't be run)
- The build_implementation function creates an implementation object that can then be used for executing code
- The prepare_state_and_params function creates a state and parameter to use for running the code, the simulation folder section explains the details more
- The rest of the code blocks show how to run different components and wirings
3. Single Simulation:
4. Experiment Simulations:

## Reports Folder

- The reports folder currently just holds one folder which is the obsidian folder
- Opening this folder up in Obsidian allows you to browse through the entire system and all components
- All of the components get refreshed every time you run the "Build Obsidian" notebook so be careful to not write any updates into this

## Simulation Folder



## Tests Folder