import math;
class LinearMath:
#Jeewan Kalia
    #Addition and Subtraction of Vectors.
    vector1 =[-8.987, -9.838, 5.031];
    vector2 = [-4.268, -1.861, -8.866];
    MaxRange = len(vector2);
    vector3 = 0.493;
    change = round((math.acos(vector3)),3);
    change = change * 180/3.14;
    print("change" + str(change));
    for number in range (MaxRange):
            SumVector = round((vector1[number] + vector2[number]),3);
            print(SumVector);

    #Scalar multiplication
    ScaleVal =float(input("input the scaling value \n"));
    ScaledVector1 = [0.00 for i in range(MaxRange)];
    ScaledVector2 = [0.00 for i in range(MaxRange)];
    for number in range (MaxRange):
            ScaledVector1[number] = round((ScaleVal * vector1[number]),3);
            ScaledVector2[number] = round((ScaleVal * vector2[number]),3);
    print("Scaled Vector 1");
    for number in range(MaxRange):
            print(ScaledVector1);
    print("Scaled Vector 2");
    for number in range(MaxRange):
            print(ScaledVector2);
    #Magnitude
    Magnitude1 = 0.00;
    Magnitude2 = 0.00;
    for number in range(MaxRange):
            Magnitude1 += round((vector1[number]*vector1[number]),3);
            Magnitude2 += round((vector2[number]*vector2[number]),3);
    Magnitude1 = round((math.sqrt(Magnitude1)),3);
    Magnitude2 = round((math.sqrt(Magnitude2)),3);
    print("The Magnitude is " + str(Magnitude1)+"\n");
    print("The Magnitude is " + str(Magnitude2)+"\n");


    #Normalization/Direction
     #Call Magnitude
    NormalizedVector1 = [0.00 for i in range(MaxRange)];
    NormalizedVector2 = [0.00 for i in range(MaxRange)];
    InverseMag1 = 1/ Magnitude1;
    InverseMag2 = 1/ Magnitude2;
    for number in range(MaxRange):
            NormalizedVector1[number] = round((InverseMag1 * vector1[number]),3); #scalar multiplication of inverse magnitude
            NormalizedVector2[number] = round((InverseMag2 * vector2[number]),3);
    print("Normalized Vector 1 \n");
    print(NormalizedVector1);
    print("Normalized Vector 2 \n");
    print(NormalizedVector2);
    #DOT product
    Dotproduct = 0.00;
    for number in range(MaxRange):
            Dotproduct += round((vector1[number] * vector2[number]),3);
    print("The Dot Product is " + str(Dotproduct) +"\n");

    #Finding theta
     #Call Normalization
    VectorAngleRadians = 0.00;
    VectorAngle = 0.00;
    Pie = 3.141; SemiCircle =180;
    for number in range(MaxRange):
            VectorAngle += round((NormalizedVector1[number] * NormalizedVector2[number]),3);# Normalized Function
    VectorAngleRadians = round(math.acos(VectorAngle),3);
    print("The radian value is " + str(VectorAngleRadians));
    VectorAngleDegrees = round((VectorAngleRadians *(SemiCircle/Pie)),3);
    print("Angle in Degrees is " + str(VectorAngleDegrees) + "\n");


    # Parallelism
    check = set();
    for number in range(MaxRange):
            check.add(round(abs(vector1[number]) / abs(vector2[number]),3));
    if len(check) == 1:
            print("Parallel");

    #Orthogonal
      #Call Dot Product
    if(not Dotproduct):
            print("Orthogonal");

    #Projection of Vectors
        #call NormalizedVector
    projectV1onV2 = [0.00 for i in range(MaxRange) ];
    product = 0.00;
    for number in range(MaxRange):
        product += round((vector1[number]* NormalizedVector2[number]),3);
    for number in range(MaxRange):
        projectV1onV2[number] = round((product * NormalizedVector2[number]),3);
    print("The projected Matrix is \n");
    print(projectV1onV2);

    #Perpendicular Vector
        #Call Project V1 on V2
    perpVector = [0.00 for i in range(MaxRange) ];
    print("Perpendicular Vector \n");
    for number in range(MaxRange):
        perpVector[number] = round((vector1[number] - projectV1onV2[number]),3);
    print(perpVector);

    #Vector V
        # Call Project V1 on V2
        # Call
    Vector1new = [0.00 for i in range(MaxRange)]
    print("Vector V");
    for number in range(MaxRange):
        Vector1new[number] = round((projectV1onV2[number] + perpVector[number]),3);
    print(Vector1new);

    #Cross Product:- only in 3D
    crossProduct=[0.00 for i in range(MaxRange)];
    pointProduct1 = 0.00;
    pointProduct2 = 0.00;
    print("Cross Product");
    for number in range(MaxRange):
        pointProduct1 = round((vector1[number-2] * vector2[number-1]),3);
        pointProduct2 = round((vector2[number-2] * vector1[number-1]),3);
        crossProduct[number] = round((pointProduct1 - pointProduct2),3);
    print(crossProduct);

    #Area of Paralleogram
        #Call Magnitude
    print("Area of Parallelogram");
    areaParallelogram = Magnitude1 * Magnitude2;
    print(areaParallelogram);

    # Area of Triangle
        #Call Parallelogram
    print("Area of Triangle");
    areaTriangle = round((0.5 * areaParallelogram),3);
    print(areaTriangle);
