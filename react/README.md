# React


## Creating app with Typescript template
```shell
npx create-react-app timeline-app --template typescript
```


## Console logs for components (inside .tsx files)
```typescript jsx
const component = () => {
    window['console'].log('Example of console log inside component');
    return (
        <div>Component</div>
    )
}
```