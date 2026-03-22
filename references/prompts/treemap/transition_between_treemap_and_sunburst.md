## 图表类型：矩形树图和旭日图的动画过渡 (Transition between Treemap and Sunburst)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/echarts-package-size.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：name, size, children, value。数据截取示例：
{
  "name": "echarts",
  "size": 3835461,
  "children": [
    {
      "name": "action",
      "size": 2307,
      "children": [
        {
          "name": "action/roamHelper.ts",
          "size": 2307,
          "value": 2307
        }
      ],
      "value": 2307
    },
    {
      "name": "animation",
      "size": 44515,
      "children": [
        {
          "name": "animation/basicTrasition.ts",
          "size": 11322,
          "value": 11322
        },
        {
          "name": "ani...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(
  ROOT_PATH + '/data/asset/data/echarts-package-size.json',
  function (data) {
    const treemapOption = {
      series: [
        {
          type: 'treemap',
          id: 'echarts-package-size',
          animationDurationUpdate: 1000,
          roam: false,
          nodeClick: undefined,
          data: data.children,
          universalTransition: true,
          label: {
            show: true
          },
          breadcrumb: {
            show: false
          }
        }
      ]
    };
    const sunburstOption = {
      series: [
        {
          type: 'sunburst',
          id: 'echarts-package-size',
          radius: ['20%', '90%'],
          animationDurationUpdate: 1000,
          nodeClick: undefined,
          data: data.children,
          universalTransition: true,
          itemStyle: {
            borderWidth: 1,
            borderColor: 'rgba(255,255,255,.5)'
          },
          label: {
            show: false
          }
        }
      ]
    };
    let currentOption = treemapOption;
    myChart.setOption(currentOption);
    setInterval(function () {
      currentOption =
        currentOption === treemapOption ? sunburstOption : treemapOption;
      myChart.setOption(currentOption);
    }, 3000);
  }
);
```

