## 图表类型：各国人均寿命与GDP关系演变 (Life Expectancy and GDP)

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
myChart.showLoading();
$.get(ROOT_PATH + '/data/asset/data/life-expectancy.json', function (data) {
  myChart.hideLoading();
  var itemStyle = {
    opacity: 0.8
  };
  var sizeFunction = function (x) {
    var y = Math.sqrt(x / 5e8) + 0.1;
    return y * 80;
  };
  // Schema:
  var schema = [
    { name: 'Income', index: 0, text: '人均收入', unit: '美元' },
    { name: 'LifeExpectancy', index: 1, text: '人均寿命', unit: '岁' },
    { name: 'Population', index: 2, text: '总人口', unit: '' },
    { name: 'Country', index: 3, text: '国家', unit: '' }
  ];
  option = {
    baseOption: {
      timeline: {
        axisType: 'category',
        orient: 'vertical',
        autoPlay: true,
        inverse: true,
        playInterval: 1000,
        left: null,
        right: 0,
        top: 20,
        bottom: 20,
        width: 55,
        height: null,
        symbol: 'none',
        checkpointStyle: {
          borderWidth: 2
        },
        controlStyle: {
          showNextBtn: false,
          showPrevBtn: false
        },
        data: []
      },
      title: [
        {
          text: data.timeline[0],
          textAlign: 'center',
          left: '63%',
          top: '55%',
          textStyle: {
            fontSize: 100
          }
        },
        {
          text: '各国人均寿命与GDP关系演变',
          left: 'center',
          top: 10,
          textStyle: {
            fontWeight: 'normal',
            fontSize: 20
          }
        }
      ],
      tooltip: {
        padding: 5,
        borderWidth: 1,
        formatter: function (obj) {
          var value = obj.value;
          // prettier-ignore
          return schema[3].text + '：' + value[3] + '<br>'
                        + schema[1].text + '：' + value[1] + schema[1].unit + '<br>'
                        + schema[0].text + '：' + value[0] + schema[0].unit + '<br>'
                        + schema[2].text + '：' + value[2] + '<br>';
        }
      },
      grid: {
        top: 100,
        containLabel: true,
        left: 30,
        right: '110'
      },
      xAxis: {
        type: 'log',
        name: '人均收入',
        max: 100000,
        min: 300,
        nameGap: 25,
        nameLocation: 'middle',
        nameTextStyle: {
          fontSize: 18
        },
        splitLine: {
          show: false
        },
        axisLabel: {
          formatter: '{value} $'
        }
      },
      yAxis: {
        type: 'value',
        name: '平均寿命',
        max: 100,
        nameTextStyle: {
          fontSize: 18
        },
        splitLine: {
          show: false
        },
        axisLabel: {
          formatter: '{value} 岁'
        }
      },
      visualMap: [
        {
          show: false,
          dimension: 3,
          categories: data.counties,
          inRange: {
            color: (function () {
              // prettier-ignore
              var colors = [ /* 请使用用户的真实数据数组替换此处 */ ];
              return colors.concat(colors);
            })()
          }
        }
      ],
      series: [
        {
          type: 'scatter',
          itemStyle: itemStyle,
          data: data.series[0],
          symbolSize: function (val) {
            return sizeFunction(val[2]);
          }
        }
      ],
      animationDurationUpdate: 1000,
      animationEasingUpdate: 'quinticInOut'
    },
    options: []
  };
  for (var n = 0; n < data.timeline.length; n++) {
    option.baseOption.timeline.data.push(data.timeline[n]);
    option.options.push({
      title: {
        show: true,
        text: data.timeline[n] + ''
      },
      series: {
        name: data.timeline[n],
        type: 'scatter',
        itemStyle: itemStyle,
        data: data.series[n],
        symbolSize: function (val) {
          return sizeFunction(val[2]);
        }
      }
    });
  }
  myChart.setOption(option);
});
```

