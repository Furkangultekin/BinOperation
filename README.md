# BinOperation

It is a basic django backend project named BinOperation for Bins and Operaitons.

## README Table of Content
- Project Set-up
- Django Application
- REST api requests and responses
- Models
- ER diagram

## Project Set-up

After downloading the project, run the commands below in the project folder, respectively:
```
$ python -m venv venv
```
```
$ venv/Scripts/activate
```
```
$ python manage.py runserver
```

## Django Application

  The project named BinOperation includes following app:
  - bin_ops : It is includes three models; Bin, Operation and BinOperation. Add and Get operations can be applied to them.

## REST api requests and responses:
### Add new bin: 
#### request: POST /bin_ops/add_bin
##### Body:
```
{
    "bin_id":3,
    "latitude":44.44,
    "longitude":55.55
}
```

### Get all bins: 
#### request: GET /bin_ops/get_bin
##### responses:
```                  
{                             
    "bin_id":3,               
    "latitude":44.44,         
    "longitude":55.55         
},                            
{                             
    "bin_id": 1,              
    "latitude": "23.23",      
    "longitude": "44.55"      
},                            
...                           
```  

### Add new operation: 
#### request: POST /bin_ops/add_operation
##### body:
```
{                                
    "operation_id":1,          
    "name":"first_operation"   
}                              
```

### Get All operations
#### request: GET /bin_ops/get_operation
##### responses:
```
[                                  
     {                             
         "operation_id": 1,        
         "name": "first_operation" 
     },                            
     {                             
         "operation_id": 2,        
         "name": "second_operation"
     },                            
     ...                           
]                                 
```

### Add new bin-operation pair
#### request: POST /bin_ops/add_bin_ops
##### body:
```
{                            
     "bin":1,                
     "operation":2,          
     "collection_frequency":3
 }                           
```
##### response:
```
{                                                    
     "bin": 1,                                       
     "operation": 2,                                 
     "collection_frequency": 3,                      
     "last_collection": "2022-05-20T00:05:33.723524Z"
 }                                                   
```

### Get all bin-operation pairs
#### request: GET /bin_ops/get_bin_ops 
##### response:
```
[                                                         
     {                                                    
         "bin": 1,                                        
         "operation": 2,                                  
         "collection_frequency": 3,                       
         "last_collection": "2022-05-20T00:05:33.723524Z" 
     },                                                   
     {                                                    
         "bin": 2,                                        
         "operation": 1,                                  
         "collection_frequency": 5,                       
         "last_collection": "2022-05-20T00:06:58.647883Z" 
     },                                                   
     ...                                                  
]                                                        
```

### Get collection frequency of all bin-operation pairs
#### request: GET /bin_ops/get_col_freq
##### response:
```
[                                             
     {                                        
         "bin": 1,                            
         "operation": 2,                      
         "collection_frequency": 3,           
         "operation_name": "second_operation" 
     },                                       
     {                                        
         "bin": 2,                            
         "operation": 1,                      
         "collection_frequency": 5,           
         "operation_name": "first_operation"  
     }                                        
 ]                                            
```

## Models

### Bin
| bin_id        | PK         |
|:------------- | :--------- |
| latitude      | FloatField |
| longitude     | FloatField |

### Operation
| operation_id  | PK           |
|:------------- | :----------- |
| name          | CharField    |

### BinOperation
| bin                  | FK            |
|:-------------        | :---------    |
| operation            | FK            |
| collection_frequency | IntegerField  |
| last_collection      | DatetimeField |

## ER diagram

![BinOperation](https://user-images.githubusercontent.com/48828422/169428855-5b17df32-419f-44fa-804c-b78c844bb9e6.png)




