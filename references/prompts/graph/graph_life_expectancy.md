## 图表类型：预期寿命 (Graph Life Expectancy)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/life-expectancy.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：counties, timeline, series。数据截取示例：
{
  "counties": [
    "China",
    "United States",
    "United Kingdom",
    "Russia",
    "India",
    "France",
    "Germany",
    "Australia",
    "Canada",
    "Cuba",
    "Finland",
    "Iceland",
    "Japan",
    "North Korea",
    "South Korea",
    "New Zealand",
    "Norway",
    "Poland",
    "Turkey"
  ],
  "timeline": [
    1800,
    1810,
    1820,
    1830,
    1840,
    1850,
    1860,
    1870,
    1880,
    1890,
    1900,
    1910,
    1920,
    1930,
    1940,
    1950,
    1...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.get(ROOT_PATH + '/data/asset/data/life-expectancy.json', function (rawData) {
  const series = [];
  rawData.counties.forEach(function (country) {
    const data = rawData.series.map(function (yearData) {
      const item = yearData.filter(function (item) {
        return item[3] === country;
      })[0];
      return {
        label: {
          show: +item[4] % 20 === 0 && +item[4] > 1940,
          position: 'top'
        },
        emphasis: {
          label: {
            show: true
          }
        },
        name: item[4],
        value: item
      };
    });
    var links = data.map(function (item, idx) {
      return {
        source: idx,
        target: idx + 1
      };
    });
    links.pop();
    series.push({
      name: country,
      type: 'graph',
      coordinateSystem: 'cartesian2d',
      data: data,
      links: links,
      edgeSymbol: ['none', 'arrow'],
      edgeSymbolSize: 5,
      legendHoverLink: false,
      lineStyle: {
        color: '#333'
      },
      itemStyle: {
        borderWidth: 1,
        borderColor: '#333'
      },
      label: {
        color: '#333',
        position: 'right'
      },
      symbolSize: 10,
      animationDelay: function (idx) {
        return idx * 100;
      }
    });
  });
  option = {
    visualMap: {
      show: false,
      min: 0,
      max: 100,
      dimension: 1
    },
    legend: {
      data: rawData.counties,
      selectedMode: 'single',
      right: 100
    },
    grid: {
      left: 0,
      bottom: 0,
      containLabel: true,
      top: 80
    },
    xAxis: {
      type: 'value'
    },
    yAxis: {
      type: 'value',
      scale: true
    },
    toolbox: {
      feature: {
        dataZoom: {}
      }
    },
    dataZoom: {
      type: 'inside'
    },
    series: series
  };
  myChart.setOption(option);
});
```

