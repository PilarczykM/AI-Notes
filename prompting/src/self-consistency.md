# Self-Consistency

Enhances the Chain-of-Thought (CoT) method by generating multiple independent reasoning paths for the same problem and then selecting the most frequently occurring or most confident answer. This technique is particularly useful for complex reasoning tasks, such as mathematical problem-solving, logical inference, and commonsense reasoning.

**How It Works:**
* The model generates multiple diverse reasoning traces for the same question.
* The most common or most confident answer is selected as the final output.
* This reduces reliance on a single reasoning chain, leading to more reliable answers.

## Example 1:
*Mathematical Reasoning*
```
Question: When I was 6, my sister was half my age. Now I'm 70; how old is my sister?
```

*Reasoning Paths:*
```
Path 1: When I was 6, my sister was 3 (half of 6). The age difference is 3 years. Now, at 70, my sister is 70 - 3 = 67.

Path 2: At age 6, my sister was 3. The difference is 3 years. Therefore, at 70, my sister is 67.

Path 3: When I was 6, my sister was 3. Now, I'm 70, so my sister is 70 - 3 = 67.
```
*Final Answer: 67 years old (consistent across all reasoning paths).*

## Example 2:
*Logical* Inference
```
Question: If a train leaves at 5 PM and takes 3 hours to reach its destination, what time does it arrive?
```
*Reasoning Paths:*
```
Path 1: 5 PM plus 3 hours equals 8 PM.

Path 2: Starting at 5 PM, after 1 hour it's 6 PM, after 2 hours it's 7 PM, and after 3 hours it's 8 PM.

Path 3: In 24-hour format, 5 PM is 17:00. Adding 3 hours results in 20:00, which is 8 PM.
```
*Final Answer: 8 PM (agreement among all paths).*


# Prompt example:
```md
You will generate multiple independent reasoning paths for a given problem. Instead of relying on a single reasoning chain, you will create diverse thought processes and derive the most consistent answer.  

- Decompose the problem into multiple logical reasoning paths.  
- Ensure that each path is distinct and explores the problem differently.  
- At the end, identify the most commonly occurring or most confident answer.  

## Examples:

### **Example 1: Mathematical Reasoning**  
**Question:** A store sells apples at $2 each and bananas at $3 each. If I buy 4 apples and 3 bananas, how much do I pay in total?  

**Reasoning Paths:**  
- **Path 1:** The cost of 4 apples is \(4 \times 2 = 8\). The cost of 3 bananas is \(3 \times 3 = 9\). Total cost = \(8 + 9 = 17\).  
- **Path 2:** Breaking it down, two apples cost $4, four apples cost $8. Three bananas cost $9. Total = $8 + $9 = $17.  
- **Path 3:** Estimate: 4 apples at $2 is about $8. Three bananas at $3 is about $9. Together, they cost $17.  

**Final Answer:** $17 (as all paths converge on the same result).  

---

### **Example 2: Logical Inference**  
**Question:** If a car travels at 60 mph for 2.5 hours, how far does it travel?  

**Reasoning Paths:**  
- **Path 1:** Distance = Speed × Time = \(60 \times 2.5 = 150\) miles.  
- **Path 2:** Breaking it down, 60 miles per hour for 2 hours is \(120\) miles, and 0.5 hours adds \(30\) more miles. Total = \(120 + 30 = 150\).  
- **Path 3:** Using fractions, \(60 \times \frac{5}{2} = 150\) miles.  

**Final Answer:** 150 miles.  

---

### **Example 3: Commonsense Reasoning**  
**Question:** Can a person run 10 miles without stopping?  

**Reasoning Paths:**  
- **Path 1:** Most people without training cannot run 10 miles non-stop due to endurance limits.  
- **Path 2:** Athletes or trained runners can complete 10 miles, but an average untrained person would struggle.  
- **Path 3:** If someone has some running experience, they might pace themselves and finish, but it would be difficult.  

**Final Answer:** **It depends on fitness level, but for an average person, it's unlikely.**  

---

## **Now, Your Turn:**  

**Question:** `{{question}}`  

**Reasoning Paths:**  
1.  
2.  
3.  

**Final Answer:**  

---
```