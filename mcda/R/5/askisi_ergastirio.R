attach(iris);
x<-Sepal.Width[Species=="setosa"];
y<-Sepal.Width[Species=="versicolor"];
z<-Sepal.Width[Species=="virginica"];
w<-Petal.Length[Species=="setosa"];
t.test(x, y);
t.test(x, y, paired=TRUE);
t.test(x, z);
t.test(x, z, paired=TRUE);
t.test(x, w);
t.test(x, w, paired=TRUE);

# Φόρτωση και ορισμός μεταβλητών
data(iris)
x <- iris$Sepal.Width[iris$Species == "setosa"]
y <- iris$Sepal.Width[iris$Species == "versicolor"]
z <- iris$Sepal.Width[iris$Species == "virginica"]
w <- iris$Petal.Length[iris$Species == "setosa"]

# 1. Έλεγχοι για ανεξάρτητα δείγματα
shapiro.test(x)
shapiro.test(y)
shapiro.test(z)

# 2. Έλεγχος για εξαρτημένα δείγματα (έλεγχος των διαφορών)
shapiro.test(x - w)

qqnorm(x);
qqline(x);