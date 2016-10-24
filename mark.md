# 配置case的参数介绍

* element_info: cn.ibona.t1_beta:id/GroupPersonItemPosition  
	* 主要填入的是元素的具体信息，如xpah,id,name等信息
* find_type: by_id
	* find的类型
	
	```
	find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
	```
	
* operate_type: click
	* 填入的操作信息
	
	```
	SEND_KEYS = "send_keys" 输入
    TAP = "tap"
    SWIPELEFT = "swipeLeft" 左滑动,一般还有配置time参数（左滑次数）
	CLICK = "click"
	```
* text: 1111111   此参数一般与send_keys配套，表示输入的参数
* index: 0 此参数一般与find_type配置里面的ids,names,xpaths等一组文件配套使用
* test_id: 1003  用例id
* test_intr: 个人反馈  用例介绍

# 其他说明
* 第一部分用例是用例的开始，需要配置用例的id,介绍等信息，其他数据一样
* 中间部分可以多个用例，不限制
* 最后一个用例是整个用例的检查点



