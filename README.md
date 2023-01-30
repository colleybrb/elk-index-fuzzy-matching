# elk-index-fuzzy-matching
Need: You have a bunch of indexes and nerfed permissions to search for fields in ELK. E.G. threat hunting on a customers elk. You want to integrate some SOC prime alerts but don't know if the customer has the values. You also cannot run the Get commands against "console" to show all the fields.

![image](https://user-images.githubusercontent.com/50241257/215595445-ce12b1f0-0378-48ab-b2fc-efbabc87b625.png)


### Operational overview
* 1. Go to each elk index copy the json from one log, and put in indices folder with index as name.
* 2. Change paths in elastic_index_fields.py
* 3. Run elastic_index_fields
* 4. Save the fields you are looking at into a fields.txt file.
* 5. Adjust the path in the fuzzymatch.py file
* 6. Set your confidence thresholds "70,80,90"
* 7. Run fuzzymatch


### Contact
***If you have issues and need help reach out to colleybrb@gmail.com


[MIT](https://choosealicense.com/licenses/mit/)
