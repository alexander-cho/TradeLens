using Microsoft.EntityFrameworkCore;
using TradeLensAPI.DbContexts;
using TradeLensAPI.Services;

var builder = WebApplication.CreateBuilder(args);

// https://www.npgsql.org/doc/release-notes/6.0.html#migrating-columns-from-timestamp-to-timestamptz
AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle

// register db context with DI
// var dbPassword = builder.Configuration["ConnectionStrings:DefaultConnection:POSTGRESPASSWORD"];
// var baseConnectionString = builder.Configuration.GetConnectionString("DefaultConnection");
// // append postgres passowrd stored in 
// var connectionStringWithPassword = $"{baseConnectionString}; Password={dbPassword}";
// Register the DbContext with the modified connection string
// builder.Services.AddDbContext<ApiDbContext>(options =>
//     options.UseNpgsql(connectionStringWithPassword));
builder.Services.AddDbContext<ApiDbContext>();

// enable CORS
var MyAllowSpecificOrigins = "_myAllowSpecificOrigins";
builder.Services.AddCors(options =>
{
    options.AddPolicy(name: MyAllowSpecificOrigins,
                      policy =>
                      {
                          policy.WithOrigins("http://localhost:3000")
                          .AllowAnyHeader()
                          .AllowAnyMethod();
                      });
});

builder.Services.AddControllers();
builder.Services.AddDbContext<ApiDbContext>(options =>
    options.UseInMemoryDatabase("Posts"));
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddHttpClient();

// register data fetching services
builder.Services.AddTransient<PolygonService>();
builder.Services.AddTransient<AlphaVantageService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors(MyAllowSpecificOrigins);

app.UseAuthorization();

app.UseHttpsRedirection();

app.MapControllers();

app.Run();
