# React


## Creating app with Typescript template
```shell
npx create-react-app app-name --template typescript
```
Replace _app-name_ with name of the app.


## Console logs for components (inside .tsx files)
```typescript jsx
const component = () => {
    window['console'].log('Example of console log inside component');
    return (
        <div>Component</div>
    )
}
```
