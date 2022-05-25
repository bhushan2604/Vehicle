<?php include 'db_conn.php';?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

    <title>Main Page</title>

    <style>
      .promodel{
        display: flex;
        justify-content : center;
        align-items: center;
        flex-wrap: wrap;
        min-height: 100vh;
      }

      .alb{
        width: 300px;
        height: 300px;
        padding: 8px;
        margin: 52px;
        
      }

      .alb img{
        width: 100%;
        height: 100%;
      }
    </style>






    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Features</a>
              </li>
              <!-- <li class="nav-item">
                <a class="nav-link" href="#">Pricing</a>
              </li> -->
              <li class="nav-item">
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
              </li>
            </ul>

            <!-- <a class="su" href="/store/signUp.php">Sign Up</a>
            <a href="/store/logIn.php">Log in</a> -->
          </div>
        </div>
      </nav>



  </head>
  <body>
    
  <div class="promodel">

    <?php
    $sql1 = "Select images,date,time,status from veh ORDER BY sno DESC";
    $res = mysqli_query($conn,$sql1);

    if(mysqli_num_rows($res)>0){
      while($pro = mysqli_fetch_assoc($res)){ 
        // $contents = file_get_contents($file);
        $proimg = $pro['images']; 
        // $base64   = "data:image;base64,'.base64_encode($proimg).'"; 
        $date = $pro['date'];
        $time = $pro['time'];
        $speed = $pro['status'];
      ?>


       <?php /* 
      
       <div class="alb"> 
        <!-- <img src="<?php echo $base64; ?>" alt=""> -->
        <?php echo '<img src= "data:image;base64,'.base64_encode($proimg).'" alt="">'?>
        <p>Date: <?php echo $date; ?></p>
        <p>Time: <?php echo $time; ?></p>
        <p>Speed: <?php echo $speed; ?></p>
      </div> 
       */ ?>
      


      <div class="card" style="width: 18rem;">
      <?php echo '<img src= "data:image;base64,'.base64_encode($proimg).'" alt="">'?>
      <div class="card-body">
      <h5 class="card-title">Speed: <?php echo $speed; ?> Km/hr</h5>
      <p class="card-text">Date: <?php echo $date; ?></p>
      <p class="card-text">Time: <?php echo $time; ?></p>
      <a href="#" class="btn btn-primary">Charge Fine</a>
      </div>
      </div>

        <?php
      }
    }

    ?>

  </div>




    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
    -->
  </body>
</html>