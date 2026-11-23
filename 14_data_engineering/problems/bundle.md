save it&#x20;

Perfect. Since you've just completed NumPy, I want you to solve a focused set of exercises before moving into Deep Learning implementation.



I don't want you spending another 2–3 weeks doing unnecessary NumPy exercises. The objective is to make sure you're comfortable enough with NumPy to implement neural networks from scratch.

# **NumPy: Required practice set**

Goal: Ready for Deep Learning implementation

**Total: 30 exercises | 5 levels**



Use Jupyter Notebook or Google Colab. Write every solution yourself. Don't look at solutions unless you're genuinely stuck.

## **Level 1 — Array fundamentals**

Exercises 1–6 · Essential foundations

1. Create a NumPy array containing numbers from 1 to 20.
2. Create a 3×3 matrix containing numbers from 1 to 9.
3. Print the `shape`, `ndim`, `size` and `dtype` of an array.
4. Create arrays of zeros, ones and a 4×4 identity matrix.
5. Generate 20 equally spaced numbers between 0 and 10.
6. Create a 3×4 matrix and extract its second row and third column.

## **Level 2 — Indexing, slicing and reshaping**

Exercises 7–12 · Essential for tensor manipulation

7. Create an array containing numbers from 1 to 12 and reshape it into a 3×4 matrix.
8. Extract the first two rows of a 3×4 matrix.
9. Extract the last two columns of a matrix.
10. Reverse a NumPy array without using a loop.
11. Flatten a 3×3 matrix into a one-dimensional array.
12. Transpose a 3×4 matrix and verify its new shape.

## **Level 3 — Mathematical operations**

Exercises 13–18 · Essential for neural networks

13. Add, subtract, multiply and divide two NumPy arrays element-wise.
14. Calculate the sum, mean, minimum and maximum of an array.
15. Calculate the mean of every row and every column of a 3×3 matrix.
16. Calculate the standard deviation and variance of an array.
17. Multiply two matrices using `np.matmul()`.
18. Calculate the dot product of two vectors.

## **Level 4 — Advanced NumPy operations**

Exercises 19–24 · Particularly important for Deep Learning

19. Generate 100 random numbers using NumPy.
20. Create an array and extract all values greater than 50 using Boolean masking.
21. Replace all negative numbers in an array with zero.
22. Use broadcasting to add a 1D array to every row of a 2D matrix.
23. Normalize an array using its mean and standard deviation.
24. Create a 5×5 matrix and calculate the sum along `axis=0` and `axis=1`.

## **Level 5 — Deep Learning preparation**

Exercises 25–30 · Your readiness checkpoint



These exercises are especially important. Don't skip them.



**25. Implement a weighted sum**



Given:

- Inputs: `[2, 3, 4]`
- Weights: `[0.5, 0.2, 0.8]`
- Bias: `1.5`

Calculate the weighted sum of the inputs plus the bias using NumPy.



**26. Implement the ReLU activation function**



Create an array containing positive and negative numbers. Apply ReLU without using a loop.



**27. Implement the sigmoid activation function**



Implement:

\\[ \sigma(x)=\frac{1}{1+e^{-x}} \\]

Apply it to an array of five numbers.



**28. Implement a simple neuron**



Given:

- Input vector with 3 features.
- Weight vector with 3 weights.
- One bias value.

Calculate the neuron's output using a weighted sum and ReLU activation.



**29. Implement matrix multiplication for a neural network**



Given:

- Input matrix with shape (4, 3).
- Weight matrix with shape (3, 2).
- Bias vector with shape (2,).

Calculate the output of the layer.



**30. Implement min-max normalization**



Given an array of 10 numbers, normalize its values into the range 0 to 1.

# **Your progress tracker**

**NumPy completion**

# **0/30**

**Level 1 — Array fundamentals**



Questions 1–6

0/6 completed

Mark level done

**Level 2 — Indexing and reshaping**



Questions 7–12

0/6 completed

Mark level done

**Level 3 — Mathematical operations**



Questions 13–18

0/6 completed

Mark level done

**Level 4 — Advanced NumPy**



Questions 19–24

0/6 completed

Mark level done

**Level 5 — Deep Learning preparation**



Questions 25–30

0/6 completed

Mark level done

Reset progress

*Only mark exercises complete after actually coding and testing them.*

# **How to practise**

Create a notebook:



`numpy_practice_for_deep_learning.ipynb`



For each question:

1. Read the problem.
2. Write your own code.
3. Execute it.
4. Verify the output.
5. Try changing the input values.
6. Add a short explanation in your own words.

**Important:** Don't use AI to generate the solutions before attempting them yourself. You can send me your code for review.

# **When can you move to Deep Learning?**

You don't need to become a NumPy expert first.

|   |
| - |

Skill

|   |
| - |

Required level

|   |
| - |

Array creation and manipulation

|   |
| - |

Comfortable

|   |
| - |

Indexing and slicing

|   |
| - |

Comfortable

|   |
| - |

Broadcasting

|   |
| - |

Comfortable

|   |
| - |

Matrix multiplication

|   |
| - |

Strong

|   |
| - |

Mean, variance and normalization

|   |
| - |

Comfortable

|   |
| - |

ReLU and Sigmoid

|   |
| - |

Understand and implement

|   |
| - |

Weighted sums

|   |
| - |

Strong

Once you can independently solve approximately 25–30 exercises, particularly Levels 4 and 5, you're ready.

## **What comes immediately after this?**

Your next implementation module will be:

Next milestone

# **Build a Neural Network from Scratch using NumPy**

[Forward Propagation](https://images.openai.com/static-rsc-4/-ct_klt0hcMWRVuN-0o-GrXlXKF75Bor1dGvdaTmC6lnPeCQYOiH-AsphifbkBXbYmAQwlCxD6NnhIT0xS3bTf79nPALbE4Vi342UCvRbqICbRJM3JgnEK-6AUhV1V2Nj9S3atHJsaXkQJK2OiRIzxp7-5T2ikpjdQI-w4DSSvM?purpose=inline)

[yogayu.github.io](https://yogayu.github.io/DeepLearningCourse/03/ForwardPropagation.html?utm_source=chatgpt.com)

We'll implement:

1. Artificial neuron
2. Weights and biases
3. Activation functions
4. Forward propagation
5. Loss calculation
6. Backpropagation
7. Gradient descent
8. Complete neural network training

No PyTorch initially. We'll build the fundamentals ourselves using NumPy.

**My advice:** Start with Question 1 and work sequentially. Send me your Level 1 code when you've completed it. I'll review it like a code reviewer, identify mistakes, suggest improvements and give you harder follow-up challenges where necessary.