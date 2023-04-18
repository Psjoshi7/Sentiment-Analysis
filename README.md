[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6ebMFVGY)
# IE 555 Project Proposal Template

---

## Team Members:  
- **Prajakta Joshi**, **pjoshi7@buffalo.edu** - This is the person who will submit the proposal
- **Yateen Natekar**, **yateensa@buffalo.edu**
- **Amey Ekkaldevi**, **ameybalr@buffalo.edu**
- **Dhiraj Bhandari**, **dhirajpa@buffalo.edu**

---

## Proposed Project Title

- **Inventory management System Analysis**

--- 
 
### Option 2 - Online Data Analysis

#### Data Sources
- *[Provide a description of each data source you plan to use.]*
    - *[For each data source, provide a link to the API documentation.]*

#### Analysis Plan
- *_Analysis:
    The inventory management analysis system will involve the following analyses with the data:_*

Product performance analysis:
This analysis will help in identifying the most and least selling products, the products with high and low profit margins, and their impact on the overall revenue of the company. The following data fields will be required for this analysis:

    Product names
    SKUs (Stock Keeping Units)
    Categories
    Descriptions
    Cost price
    Selling price
    Quantity
    Sales revenue

To conduct this analysis, we can use Python's Pandas library to extract the required data from the inventory management database. We can then calculate the sales revenue and profit margins for each product and rank them based on their performance. This analysis can help in identifying the products that are driving the company's revenue and those that are not performing well. The analysis can also help in making informed decisions about pricing, promotions, and product development.

Stock level analysis:
This analysis will help in understanding the stock levels of the products and identifying the overstocked and understocked products. This analysis can further help in identifying the reorder point, safety stock level, and lead time for the products. The following data fields will be required for this analysis:

    Product names
    SKUs
    Categories
    Descriptions
    Cost price
    Selling price
    Quantity
    Reorder point
    Safety stock level
    Lead time

To conduct this analysis, we can use Python's Pandas library to extract the required data from the inventory management database. We can then calculate the stock levels for each product and compare them against the reorder point and safety stock level. This analysis can help in optimizing the inventory levels, reducing stockouts and overstocking, and improving the overall inventory management performance.

Supplier performance analysis:
This analysis will help in identifying the most and least reliable suppliers based on their delivery times, product quality, and cost-effectiveness. The following data fields will be required for this analysis:

    Supplier names
    Contact details
    Delivery times
    Product quality
    Cost-effectiveness
    Order quantities
    Lead time

To conduct this analysis, we can use Python's Pandas library to extract the required data from the inventory management database. We can then calculate the delivery times, product quality, and cost-effectiveness for each supplier and rank them based on their performance. This analysis can help in identifying the suppliers that are meeting the company's expectations and those that are not. The analysis can also help in negotiating better deals and building stronger relationships with the most reliable suppliers.

Sales analysis:
This analysis will help in understanding the sales patterns, identifying the most and least profitable sales channels, and identifying the regions with the highest and lowest sales. The following data fields will be required for this analysis:

    Sales dates
    Channels
    Regions
    Quantities sold
    Revenue generated
    Product names
    SKUs

*_To conduct this analysis, we can use Python's Pandas library to extract the required data from the inventory management database. We can then calculate the sales revenue and profit margins for each sales channel and region and rank them based on their performance. This analysis can help in identifying the most profitable sales channels and regions and focusing the company's marketing and sales efforts on them. The analysis can also help in identifying the least profitable sales channels and regions and taking corrective actions to improve their performance._*
- *[Clearly justify how the chosen source data will enable your team to conduct this analysis.]*

#### Motivation
- *_Inventory management is a vital aspect of any supply chain, especially for **electronics distributors** who deal with a vast catalog of products and a diverse customer base. Developing a Python-based inventory management analysis system can help such distributors optimize their inventory levels, improve order fulfillment, and enhance customer satisfaction. Our project aims to leverage the power of data analysis to uncover hidden patterns and insights in inventory data. By analyzing customer buying behavior and predicting future demand, we can help the distributor make informed decisions about inventory levels, ordering processes, and customer engagement.
Our team of Python programmers and data analysts is excited to take on this challenge and develop an inventory management system that will set the distributor apart from its competitors. This project offers an opportunity to showcase our skills and creativity while contributing to the success of an industry that plays a vital role in modern society. We believe that this project will provide valuable insights into supply chain management, enabling the distributor to optimize its operations and stay ahead of the curve in a rapidly evolving industry. By applying our technical expertise to this real-world business problem, we can make a meaningful contribution to the world of inventory management and enhance our skills and knowledge as data analysts and programmers._*
