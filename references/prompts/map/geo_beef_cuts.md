## 图表类型：庖丁解牛 (GEO Beef Cuts)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data/asset/geo/Beef_cuts_France.svg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.get(ROOT_PATH + '/data/asset/geo/Beef_cuts_France.svg', function (svg) {
  echarts.registerMap('Beef_cuts_France', { svg: svg });
  option = {
    tooltip: {},
    visualMap: {
      left: 'center',
      bottom: '10%',
      min: 5,
      max: 100,
      orient: 'horizontal',
      text: ['', 'Price'],
      realtime: true,
      calculable: true,
      inRange: {
        color: ['#dbac00', '#db6e00', '#cf0000']
      }
    },
    series: [
      {
        name: 'French Beef Cuts',
        type: 'map',
        map: 'Beef_cuts_France',
        roam: true,
        emphasis: {
          label: {
            show: false
          }
        },
        selectedMode: false,
        data: [ /* 请使用用户的真实数据数组替换此处 */ ]
      }
    ]
  };
  myChart.setOption(option);
});
```

