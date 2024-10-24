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

## Reports Folder

## Simulation Folder



## Tests Folder