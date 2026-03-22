## 图表类型：ECharts 配置项查询分布 (ECharts Option Query)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/ec-option-doc-statistics-201604.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：xAxis, series, visualMap, tooltip, title。数据截取示例：
{
  "xAxis": {
    "axisLabel": {
      "$count": 2534,
      "show": {
        "$count": 444
      },
      "interval": {
        "$count": 950
      },
      "rotate": {
        "$count": 584
      },
      "inside": {
        "$count": 416
      },
      "formatter": {
        "$count": 886
      },
      "textStyle": {
        "$count": 490,
        "color": {
          "$count": 142
        },
        "fontStyle": {
          "$count": 107
        },
        "fontWeight": {
          "$coun...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const uploadedDataURL =
  ROOT_PATH + '/data/asset/data/ec-option-doc-statistics-201604.json';
myChart.showLoading();
$.getJSON(uploadedDataURL, function (rawData) {
  myChart.hideLoading();
  function convert(source, target, basePath) {
    for (let key in source) {
      let path = basePath ? basePath + '.' + key : key;
      if (!key.match(/^\$/)) {
        target.children = target.children || [];
        const child = {
          name: path
        };
        target.children.push(child);
        convert(source[key], child, path);
      }
    }
    if (!target.children) {
      target.value = source.$count || 1;
    } else {
      target.children.push({
        name: basePath,
        value: source.$count
      });
    }
  }
  const data = {
    children: []
  };
  convert(rawData, data, '');
  myChart.setOption(
    (option = {
      title: {
        text: 'ECharts Options',
        subtext: '2016/04',
        left: 'leafDepth'
      },
      tooltip: {},
      series: [
        {
          name: 'option',
          type: 'treemap',
          visibleMin: 300,
          data: data.children,
          leafDepth: 2,
          levels: [
            {
              itemStyle: {
                borderColor: '#555',
                borderWidth: 4,
                gapWidth: 4
              }
            },
            {
              colorSaturation: [0.3, 0.6],
              itemStyle: {
                borderColorSaturation: 0.7,
                gapWidth: 2,
                borderWidth: 2
              }
            },
            {
              colorSaturation: [0.3, 0.5],
              itemStyle: {
                borderColorSaturation: 0.6,
                gapWidth: 1
              }
            },
            {
              colorSaturation: [0.3, 0.5]
            }
          ]
        }
      ]
    })
  );
});
```

