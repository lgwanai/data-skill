## 图表类型：2002全国宏观经济指标 (Finance Indices 2002)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var dataMap = {};
function dataFormatter(obj) {
  // prettier-ignore
  var pList = [ /* 请使用用户的真实数据数组替换此处 */ ];
  var temp;
  for (var year = 2002; year <= 2011; year++) {
    var max = 0;
    var sum = 0;
    temp = obj[year];
    for (var i = 0, l = temp.length; i < l; i++) {
      max = Math.max(max, temp[i]);
      sum += temp[i];
      obj[year][i] = {
        name: pList[i],
        value: temp[i]
      };
    }
    obj[year + 'max'] = Math.floor(max / 100) * 100;
    obj[year + 'sum'] = sum;
  }
  return obj;
}
// prettier-ignore
dataMap.dataGDP = dataFormatter({
    //max : 60000,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
// prettier-ignore
dataMap.dataPI = dataFormatter({
    //max : 4000,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
// prettier-ignore
dataMap.dataSI = dataFormatter({
    //max : 26600,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
// prettier-ignore
dataMap.dataTI = dataFormatter({
    //max : 25000,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
// prettier-ignore
dataMap.dataEstate = dataFormatter({
    //max : 3600,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
// prettier-ignore
dataMap.dataFinancial = dataFormatter({
    //max : 3200,
    2011: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2010: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2009: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2008: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2007: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2006: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2005: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2004: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2003: [ /* 请使用用户的真实数据数组替换此处 */ ],
    2002: [ /* 请使用用户的真实数据数组替换此处 */ ]
});
option = {
  baseOption: {
    timeline: {
      axisType: 'category',
      // realtime: false,
      // loop: false,
      autoPlay: true,
      // currentIndex: 2,
      playInterval: 1000,
      // controlStyle: {
      //     position: 'left'
      // },
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      label: {
        formatter: function (s) {
          return new Date(s).getFullYear();
        }
      }
    },
    title: {
      subtext: '数据来自国家统计局'
    },
    tooltip: {},
    legend: {
      left: 'right',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      selected: {
        GDP: false,
        金融: false,
        房地产: false
      }
    },
    calculable: true,
    grid: {
      top: 80,
      bottom: 100,
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow',
          label: {
            show: true,
            formatter: function (params) {
              return params.value.replace('\n', '');
            }
          }
        }
      }
    },
    xAxis: [
      {
        type: 'category',
        axisLabel: { interval: 0 },
        data: [ /* 请使用用户的真实数据数组替换此处 */ ],
        splitLine: { show: false }
      }
    ],
    yAxis: [
      {
        type: 'value',
        name: 'GDP（亿元）'
      }
    ],
    series: [
      { name: 'GDP', type: 'bar' },
      { name: '金融', type: 'bar' },
      { name: '房地产', type: 'bar' },
      { name: '第一产业', type: 'bar' },
      { name: '第二产业', type: 'bar' },
      { name: '第三产业', type: 'bar' },
      {
        name: 'GDP占比',
        type: 'pie',
        center: ['75%', '35%'],
        radius: '28%',
        z: 100
      }
    ]
  },
  options: [
    {
      title: { text: '2002全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2002'] },
        { data: dataMap.dataFinancial['2002'] },
        { data: dataMap.dataEstate['2002'] },
        { data: dataMap.dataPI['2002'] },
        { data: dataMap.dataSI['2002'] },
        { data: dataMap.dataTI['2002'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2002sum'] },
            { name: '第二产业', value: dataMap.dataSI['2002sum'] },
            { name: '第三产业', value: dataMap.dataTI['2002sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2003全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2003'] },
        { data: dataMap.dataFinancial['2003'] },
        { data: dataMap.dataEstate['2003'] },
        { data: dataMap.dataPI['2003'] },
        { data: dataMap.dataSI['2003'] },
        { data: dataMap.dataTI['2003'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2003sum'] },
            { name: '第二产业', value: dataMap.dataSI['2003sum'] },
            { name: '第三产业', value: dataMap.dataTI['2003sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2004全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2004'] },
        { data: dataMap.dataFinancial['2004'] },
        { data: dataMap.dataEstate['2004'] },
        { data: dataMap.dataPI['2004'] },
        { data: dataMap.dataSI['2004'] },
        { data: dataMap.dataTI['2004'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2004sum'] },
            { name: '第二产业', value: dataMap.dataSI['2004sum'] },
            { name: '第三产业', value: dataMap.dataTI['2004sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2005全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2005'] },
        { data: dataMap.dataFinancial['2005'] },
        { data: dataMap.dataEstate['2005'] },
        { data: dataMap.dataPI['2005'] },
        { data: dataMap.dataSI['2005'] },
        { data: dataMap.dataTI['2005'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2005sum'] },
            { name: '第二产业', value: dataMap.dataSI['2005sum'] },
            { name: '第三产业', value: dataMap.dataTI['2005sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2006全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2006'] },
        { data: dataMap.dataFinancial['2006'] },
        { data: dataMap.dataEstate['2006'] },
        { data: dataMap.dataPI['2006'] },
        { data: dataMap.dataSI['2006'] },
        { data: dataMap.dataTI['2006'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2006sum'] },
            { name: '第二产业', value: dataMap.dataSI['2006sum'] },
            { name: '第三产业', value: dataMap.dataTI['2006sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2007全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2007'] },
        { data: dataMap.dataFinancial['2007'] },
        { data: dataMap.dataEstate['2007'] },
        { data: dataMap.dataPI['2007'] },
        { data: dataMap.dataSI['2007'] },
        { data: dataMap.dataTI['2007'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2007sum'] },
            { name: '第二产业', value: dataMap.dataSI['2007sum'] },
            { name: '第三产业', value: dataMap.dataTI['2007sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2008全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2008'] },
        { data: dataMap.dataFinancial['2008'] },
        { data: dataMap.dataEstate['2008'] },
        { data: dataMap.dataPI['2008'] },
        { data: dataMap.dataSI['2008'] },
        { data: dataMap.dataTI['2008'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2008sum'] },
            { name: '第二产业', value: dataMap.dataSI['2008sum'] },
            { name: '第三产业', value: dataMap.dataTI['2008sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2009全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2009'] },
        { data: dataMap.dataFinancial['2009'] },
        { data: dataMap.dataEstate['2009'] },
        { data: dataMap.dataPI['2009'] },
        { data: dataMap.dataSI['2009'] },
        { data: dataMap.dataTI['2009'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2009sum'] },
            { name: '第二产业', value: dataMap.dataSI['2009sum'] },
            { name: '第三产业', value: dataMap.dataTI['2009sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2010全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2010'] },
        { data: dataMap.dataFinancial['2010'] },
        { data: dataMap.dataEstate['2010'] },
        { data: dataMap.dataPI['2010'] },
        { data: dataMap.dataSI['2010'] },
        { data: dataMap.dataTI['2010'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2010sum'] },
            { name: '第二产业', value: dataMap.dataSI['2010sum'] },
            { name: '第三产业', value: dataMap.dataTI['2010sum'] }
          ]
        }
      ]
    },
    {
      title: { text: '2011全国宏观经济指标' },
      series: [
        { data: dataMap.dataGDP['2011'] },
        { data: dataMap.dataFinancial['2011'] },
        { data: dataMap.dataEstate['2011'] },
        { data: dataMap.dataPI['2011'] },
        { data: dataMap.dataSI['2011'] },
        { data: dataMap.dataTI['2011'] },
        {
          data: [
            { name: '第一产业', value: dataMap.dataPI['2011sum'] },
            { name: '第二产业', value: dataMap.dataSI['2011sum'] },
            { name: '第三产业', value: dataMap.dataTI['2011sum'] }
          ]
        }
      ]
    }
  ]
};
```

