## 图表类型：多数值轴轴缩放 (Mix Zoom On Value)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/obama_budget_proposal_2012.list.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：budget2012List, budget2011List, delta, names。数据截取示例：
{
  "budget2012List": [
    0,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    1000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    2000,
    3000,
    3000,
    3000,
    3000,
    3000,
    3000,
    3000,
    4000,
    4000,
    4000,
    4000,
    5000,
    5000,
    5000,
    5000,
    6000,
    6000,
    6000,
    6000,
    6000,
    7000,
    7000,
    7000,
    8000,
    8000,...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
$.get(
  ROOT_PATH + '/data/asset/data/obama_budget_proposal_2012.list.json',
  function (obama_budget_2012) {
    myChart.hideLoading();
    option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow',
          label: {
            show: true
          }
        }
      },
      toolbox: {
        show: true,
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          magicType: { show: true, type: ['line', 'bar'] },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      calculable: true,
      legend: {
        data: ['Growth', 'Budget 2011', 'Budget 2012'],
        itemGap: 5
      },
      grid: {
        top: '12%',
        left: '1%',
        right: '10%',
        containLabel: true
      },
      xAxis: [
        {
          type: 'category',
          data: obama_budget_2012.names
        }
      ],
      yAxis: [
        {
          type: 'value',
          name: 'Budget (million USD)',
          axisLabel: {
            formatter: function (a) {
              a = +a;
              return isFinite(a) ? echarts.format.addCommas(+a / 1000) : '';
            }
          }
        }
      ],
      dataZoom: [
        {
          show: true,
          start: 94,
          end: 100
        },
        {
          type: 'inside',
          start: 94,
          end: 100
        },
        {
          show: true,
          yAxisIndex: 0,
          filterMode: 'empty',
          width: 30,
          height: '80%',
          showDataShadow: false,
          left: '93%'
        }
      ],
      series: [
        {
          name: 'Budget 2011',
          type: 'bar',
          data: obama_budget_2012.budget2011List
        },
        {
          name: 'Budget 2012',
          type: 'bar',
          data: obama_budget_2012.budget2012List
        }
      ]
    };
    myChart.setOption(option);
  }
);
```

